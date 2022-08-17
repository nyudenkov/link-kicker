from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode

from app.bot.dialogs import TimezoneDialogSG
from app.database.models import User


async def timezone_handler(message: types.Message, dialog_manager: DialogManager):
    await User.get_from_message(message)
    await dialog_manager.start(TimezoneDialogSG.main, mode=StartMode.RESET_STACK)
