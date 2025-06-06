from aiogram import types
from loguru import logger

from app import config
from app.bot import bot
from app.database.models import User


async def mailing_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    if user.tg_id != config.ADMIN_CHAT_ID:
        await message.reply("No access")
        return

    for user in await User.all():
        try:
            await bot.send_message(
                user.tg_id, message.text.removeprefix("/admin_mailing ")
            )
        except Exception as ex:
            logger.error(ex)
