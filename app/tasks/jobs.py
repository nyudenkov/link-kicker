from datetime import datetime

import pytz
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
    now_hour: int = datetime.now(pytz.timezone("Europe/Moscow")).hour
    for user in await User.filter(hour=now_hour):
        await send_mailing_message(user)
    if now_hour == 18:
        for user in await User.filter(hour__isnull=True):
            await send_mailing_message(user)
