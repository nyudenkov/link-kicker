from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode

from app.bot.dialogs import LanguageDialogSG
from app.bot.middlewares import i18n
from app.constants import welcome_text
from app.database.models import User

_ = i18n.gettext


async def send_welcome(message: types.Message, dialog_manager: DialogManager):
    await User.get_from_message(message)
    message = await message.reply(_(welcome_text))
    await dialog_manager.start(
        LanguageDialogSG.main,
        data={"start": True, "message_id": message.message_id},
        mode=StartMode.RESET_STACK,
    )
