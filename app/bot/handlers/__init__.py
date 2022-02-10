from aiogram import Dispatcher

from app.bot.handlers import feedback
from app.bot.handlers import hour
from app.bot.handlers import language
from app.bot.handlers import link
from app.bot.handlers import mailing
from app.bot.handlers import statistics
from app.bot.handlers.start import send_welcome


def setup(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands="start")

    dp.register_message_handler(feedback.feedback_handler, commands="feedback")

    dp.register_message_handler(hour.hour_handler, commands="hour")

    dp.register_message_handler(language.language_handler, commands="language")

    dp.register_message_handler(mailing.mailing_handler, commands="admin_mailing")

    dp.register_message_handler(statistics.statistics_handler, commands="statistics")
    dp.register_message_handler(statistics.bot_statistics_handler, commands="botstatistics")

    dp.register_message_handler(link.message_link_handler, lambda m: m.text and m.text[0] != "/")
    dp.register_message_handler(link.get_random_link_handler, commands="random")
    dp.register_message_handler(link.links_handler, commands="links")
    dp.register_message_handler(link.switch_link_mailing, commands="mailing")
    dp.register_callback_query_handler(link.del_link_handler, lambda c: c.data and c.data.startswith("del"))
    dp.register_callback_query_handler(link.read_link_handler, lambda c: c.data and c.data.startswith("read"))
    dp.register_callback_query_handler(
        link.links_page_handler, lambda c: c.data and c.data.startswith("links_paginator")
    )
    dp.register_callback_query_handler(
        link.del_link_from_links_handler, lambda c: c.data and c.data.startswith("links_del")
    )
