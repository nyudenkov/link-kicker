from aiogram import types

from app import config, enums
from app.bot.middlewares import i18n
from app.bot.utils.errors import catch_error
from app.bot.utils.statistics import catch_intent
from app.constants import Message
from app.database.models import Link, User

_ = i18n.gettext


@catch_intent(intent=enums.Intent.STATISTICS)
@catch_error
async def statistics_handler(message: types.Message):
    user, created = await User.get_from_message(message)

    all_count: int = await Link.filter(owner=user).count()
    was_read_count: int = await Link.filter(owner=user, was_read=True).count()

    await message.reply(_(Message.F_STATISTICS).format(all_count, was_read_count))


async def bot_statistics_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    if user.tg_id != config.ADMIN_CHAT_ID:
        await message.reply("No access")
        return
    all_count: int = await Link.all().count()
    was_read_count: int = await Link.filter(was_read=True).count()

    await message.reply(_(Message.F_BOT_STATISTICS).format(all_count, was_read_count))
