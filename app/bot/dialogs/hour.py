from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import Message
from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput

from app.bot.dialogs.widgets.text import IConst
from app.bot.middlewares import i18n
from app.database.models import User

_ = i18n.gettext


class HourDialogSG(StatesGroup):
    main = State()
    retry = State()


def validate_hour_input(hour: int) -> bool:
    if 0 <= hour <= 23:
        return True
    return False


async def on_hour_input(m: Message, dialog: Dialog, manager: DialogManager):
    if m.text.isnumeric():
        value = int(m.text)
        if validate_hour_input(value):
            user, created = await User.get_from_message(m)
            await user.set_hour(value)
            await m.reply(
                text=_(
                    "Начнём? Отправляй любую ссылку в диалог и получишь ее в {}:00 по Московскому времени 👇🏻"
                ).format(value) if created
                else _("Отправляй любую ссылку в диалог и получишь ее в {}:00 по Московскому времени 👇🏻").format(value)
            )
            await manager.done()
            return
    await manager.dialog().switch_to(HourDialogSG.retry)


hour_dialog = Dialog(
    Window(
        IConst(_(
            "Напиши час во сколько тебе будет удобно получать ссылочку (по Московскому времени, надо написать цифру от 0 до 23)"
        )),
        MessageInput(on_hour_input),
        state=HourDialogSG.main,
    ),
    Window(
        IConst(_("Тебе нужно написать цифру от 0 до 23")),
        MessageInput(on_hour_input),
        state=HourDialogSG.retry,
    )
)
