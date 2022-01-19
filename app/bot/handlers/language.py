from aiogram import types

from app import enums
from app.bot.forms import LanguageForm
from app.bot.forms import language_form_callback
from app.bot.utils.errors import catch_error
from app.bot.utils.statistics import catch_intent
from app.database.models import User


@catch_intent(intent=enums.Intent.LANGUAGE)
@catch_error
async def language_handler(message: types.Message):
    await User.get_from_message(message)
    await LanguageForm.start(language_form_callback)
