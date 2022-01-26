from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from app.bot.middlewares.i18n import I18nMiddleware

i18n = I18nMiddleware("link_kicker", default="en")


def setup(dispatcher: Dispatcher):
    logger.info("Configure middlewares...")

    dispatcher.middleware.setup(LoggingMiddleware("bot"))
    dispatcher.middleware.setup(i18n)
