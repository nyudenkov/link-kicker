from aiogram import types
from aiogram_dialog import DialogManager, StartMode

from app import enums
from app.bot.dialogs.feedback import FeedbackDialogSG
from app.bot.middlewares import i18n
from app.bot.utils.errors import catch_error
from app.bot.utils.statistics import catch_intent
from app.database.models import User

_ = i18n.gettext


@catch_intent(intent=enums.Intent.FEEDBACK)
@catch_error
async def feedback_handler(message: types.Message, dialog_manager: DialogManager):
    await User.get_from_message(message)
    await dialog_manager.start(FeedbackDialogSG.main, mode=StartMode.RESET_STACK)
