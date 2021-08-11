from aiogram import types

from app import enums
from app.bot.utils.statistics import catch_intent
from app.constants import Message
from app.database.models import Link
from app.database.models import User


@catch_intent(intent=enums.Intent.STATISTICS)
async def statistics_handler(message: types.Message):
    user, created = await User.get_from_message(message)

    all_count: int = await Link.filter(owner=user).count()
    was_read_count: int = await Link.filter(owner=user, was_read=True).count()

    await message.reply(Message.F_STATISTICS.format(all_count, was_read_count))


async def bot_statistics_handler(message: types.Message):
    all_count: int = await Link.all().count()
    was_read_count: int = await Link.filter(was_read=True).count()

    await message.reply(Message.F_BOT_STATISTICS.format(all_count, was_read_count))
