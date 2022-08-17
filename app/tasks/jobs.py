from datetime import datetime

from aiogram.utils import exceptions as aiogram_exceptions
from loguru import logger

from app.bot import bot
from app.bot.messages import get_random_link_message
from app.database.models import User
from app.misc.sentry import capture_exception


async def send_mailing_message(user):
    message_text, markup = await get_random_link_message(user, mailing=True)
    if not message_text:
        return

    try:
        await bot.send_message(user.tg_id, message_text, reply_markup=markup)
    except aiogram_exceptions.BotBlocked:
        logger.info(f"{user.tg_id} blocked bot")
    except Exception as ex:  # noqa
        capture_exception(ex)


async def link_mailing():
    now_hour: int = datetime.utcnow().hour
    for user in await User.filter(hour=now_hour, mailing=True):
        await send_mailing_message(user)


async def delete_message(chat_id: int, message_id: int):
    try:
        await bot.delete_message(chat_id, message_id)
    except Exception as ex:
        logger.error(ex)
