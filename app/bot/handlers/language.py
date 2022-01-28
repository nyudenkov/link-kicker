from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode
from app.bot.dialogs import LanguageDialogSG

from app import enums
from app.bot.utils import catch_error
from app.bot.utils.statistics import catch_intent
from app.database.models import User


@catch_intent(intent=enums.Intent.LANGUAGE)
@catch_error
async def language_handler(message: types.Message, dialog_manager: DialogManager):
    await User.get_from_message(message)
    await dialog_manager.start(LanguageDialogSG.main, mode=StartMode.RESET_STACK)
