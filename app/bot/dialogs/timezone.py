import datetime
import re

import pytz
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.types import ContentType
from aiogram.types import KeyboardButton
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup
from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.kbd import Group
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.when import Whenable
from babel import dates
from timezonefinder import TimezoneFinder

from app.bot.dialogs.hour import HourDialogSG
from app.bot.dialogs.widgets.text import IConst
from app.bot.dialogs.widgets.text import IFormat
from app.bot.middlewares import i18n
from app.constants import Regexp
from app.database.models import User

_ = i18n.gettext


class TimezoneDialogSG(StatesGroup):
    main = State()

    send_location = State()
    location_sent = State()

    choose_timezone = State()
    repeat_timezone_input = State()

    check_timezone = State()


async def on_send_location_clicked(m: CallbackQuery, dialog: Dialog, manager: DialogManager):
    message = await m.message.answer(
        _("Или нажми на кнопку ниже"),
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text=_("Отправить локацию"), request_location=True)]], one_time_keyboard=True
        )
    )
    manager.current_context().dialog_data['location_request_msg_id'] = message.message_id


async def delete_location_request_message(callback: CallbackQuery, dialog: Dialog, manager: DialogManager):
    msg_id = manager.current_context().dialog_data['location_request_msg_id']
    await callback.message.chat.delete_message(msg_id)


async def on_location_sent(message: Message, dialog: Dialog, manager: DialogManager):
    ctx = manager.current_context()
    user, _ = await User.get_from_message(message)

    # Here's the dumbest way to delete reply_keyboard from 'on_send_location_clicked'
    await message.chat.delete_message(ctx.dialog_data['location_request_msg_id'])

    location = message.location
    timezone_str = TimezoneFinder().certain_timezone_at(lat=location.latitude, lng=location.longitude)

    timezone_utc_offset = datetime.datetime.now(pytz.timezone(timezone_str)).utcoffset().total_seconds()/60/60
    timezone_output = dates.get_timezone_name(timezone_str, locale=user.language_iso)
    manager.current_context().dialog_data['timezone_utc_offset'] = timezone_utc_offset
    manager.current_context().dialog_data['timezone_output'] = timezone_output

    await manager.dialog().switch_to(TimezoneDialogSG.check_timezone)


async def save_timezone_on_offset_input(m: Message, dialog: Dialog, manager: DialogManager):
    if match := re.match(Regexp.NUM_WITH_SYMBOL, m.text):
        value = int(match.group())
        user, _ = await User.get_from_message(m)
        user.hour_utc_offset = value
        await user.save()

        await manager.done()
        await manager.start(HourDialogSG.main, data=True, mode=StartMode.RESET_STACK)
        return

    await manager.dialog().switch_to(TimezoneDialogSG.repeat_timezone_input)


async def save_timezone(callback: CallbackQuery, dialog: Dialog, manager: DialogManager):
    ctx = manager.current_context()

    user = await User.get(tg_id=callback.from_user.id)
    user.hour_utc_offset = ctx.dialog_data['timezone_utc_offset']
    await user.save()

    await manager.done()
    await manager.start(HourDialogSG.main, data=True, mode=StartMode.RESET_STACK)


def can_be_cancelled(data: dict, widget: Whenable, manager: DialogManager):
    return manager.current_context().start_data is None


timezone_dialog = Dialog(
    Window(
        IConst(_(
            "Отправь свою локацию чтобы определить часовой пояс или выбери вручную\n"
            "<i>В случае отправления локации боту, данные будут использованы только единожды для определения часового "
            "пояса и не будут сохранены.</i>"
        )),
        Group(
            SwitchTo(
                IConst(_("Отправить локацию")),
                id="send_location",
                state=TimezoneDialogSG.send_location,
                on_click=on_send_location_clicked
            ),
            SwitchTo(
                IConst(_("Выбрать вручную")),
                id="choose_timezone",
                state=TimezoneDialogSG.choose_timezone,
            ),
            width=2,
        ),
        Cancel(IConst(_("Отменить действие")), when=can_be_cancelled),
        state=TimezoneDialogSG.main,
    ),

    Window(
        IConst(_("Отправь свою локацию (Вложения -> Локация)")),
        SwitchTo(
            IConst(_("Вернуться назад")),
            id="back",
            on_click=delete_location_request_message,
            state=TimezoneDialogSG.main,
        ),
        MessageInput(on_location_sent, content_types=ContentType.LOCATION),
        state=TimezoneDialogSG.send_location,
    ),

    Window(
        IConst(_(
            "Напиши разницу твоего часового пояса с UTC\n"
            "Например: разница Москвы с UTC - +3 часа, надо написать <b>+3</b>; "
            "разница Нью-Йорка с UTC - -4 часа, надо написать <b>-4</b>\n"
            "Чтобы узнать разницу, можно использовать "
            "<a href='https://www.timeanddate.com/time/difference/timezone/utc'>этот сайт</a>"
        )),
        SwitchTo(
            IConst(_("Вернуться назад")),
            id="back",
            state=TimezoneDialogSG.main,
        ),
        MessageInput(save_timezone_on_offset_input),
        state=TimezoneDialogSG.choose_timezone,
    ),

    Window(
        IConst(_(
            "Произошла ошибочка! На примере с Москвой - надо написать просто <b>+3</b>; с Нью-Йорком - <b>-4</b>"
        )),
        MessageInput(save_timezone_on_offset_input),
        state=TimezoneDialogSG.repeat_timezone_input,
    ),

    Window(
        IFormat(_("Я правильно определил твой часовой пояс? <b>{timezone_output}</b>")),
        Group(
            Button(
                IConst(_("Да")),
                id='right_tz',
                on_click=save_timezone,
            ),
            SwitchTo(
                IConst(_("Нет")),
                id="back",
                state=TimezoneDialogSG.main,
            ),
            width=2,
        ),
        state=TimezoneDialogSG.check_timezone,
    ),
)
