from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Back
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.kbd import Group
from aiogram_dialog.widgets.kbd import SwitchTo

from app.bot.dialogs.widgets.text import IConst
from app.bot.dialogs.widgets.text import IFormat
from app.bot.middlewares import i18n
from app.database.models import FeedbackReport

_ = i18n.gettext


class FeedbackDialogSG(StatesGroup):
    main = State()
    receive_report = State()


async def feedback_type_chosen(callback: CallbackQuery, button: Button, manager: DialogManager):
    ctx = manager.current_context()
    type_id = button.widget_id
    ctx.dialog_data['report_type'] = type_id
    if type_id == "bug":
        ctx.dialog_data['message_state_text'] = _("найденного бага. Расскажи, как его повторить 🪳")
    elif type_id == "feature":
        ctx.dialog_data['message_state_text'] = _("своего предложения")
    else:
        await callback.message.answer(_("Возникла ошибка, сообщи @nyudenkov, пожалуйста"))


async def report_input(message: Message, dialog: Dialog, manager: DialogManager):
    ctx = manager.current_context()
    await FeedbackReport.create(
        type=ctx.dialog_data['report_type'], text=message.text
    )
    await message.answer(_("Спасибо!"))
    await manager.done()


feedback_dialog = Dialog(
    Window(
        IConst(_("Выбери чем хочешь поделиться")),
        Group(
            SwitchTo(
                IConst(_("Ошибкой")),
                id="bug",
                on_click=feedback_type_chosen,
                state=FeedbackDialogSG.receive_report,
            ),
            SwitchTo(
                IConst(_("Предложением")),
                id="feature",
                on_click=feedback_type_chosen,
                state=FeedbackDialogSG.receive_report,
            ),
            width=2,
        ),
        Cancel(IConst(_("Отменить действие"))),
        state=FeedbackDialogSG.main,
    ),
    Window(
        IFormat(_("Поделись, пожалуйста, деталями {message_state_text}")),
        Back(IConst(_("Вернуться назад"))),
        MessageInput(report_input),
        state=FeedbackDialogSG.receive_report,
    )
)
