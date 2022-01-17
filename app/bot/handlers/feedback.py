from aiogram import types

from app import enums
from app.bot.utils.errors import catch_error
from app.bot.utils.statistics import catch_intent
from app.constants import Message
from app.database.models import User


@catch_intent(intent=enums.Intent.FEEDBACK)
@catch_error
async def feedback_handler(message: types.Message):
    await User.get_from_message(message)
    await message.reply(Message.FEEDBACK)
