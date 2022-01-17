from aiogram import types

from app import enums
from app.bot.forms import HourForm
from app.bot.forms import hour_form_callback
from app.bot.utils.errors import catch_error
from app.bot.utils.statistics import catch_intent
from app.database.models import User


@catch_intent(intent=enums.Intent.HOUR)
@catch_error
async def hour_handler(message: types.Message):
    await User.get_from_message(message)
    await HourForm.start(hour_form_callback)
