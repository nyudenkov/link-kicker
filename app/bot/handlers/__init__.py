from aiogram import Dispatcher

from app.bot.handlers import feedback
from app.bot.handlers import hour
from app.bot.handlers import link
from app.bot.handlers import mailing
from app.bot.handlers import statistics
from app.bot.handlers.start import send_welcome


def setup(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands="start")

    dp.register_message_handler(
        link.link_handler,
        regexp=r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,10}(:[0-9]{1,5})?(\/.*)?$",
    )
    dp.register_message_handler(link.get_random_link_handler, commands="random")
    dp.register_callback_query_handler(
        link.del_link_handler, lambda c: c.data and c.data.startswith("del")
    )
    dp.register_callback_query_handler(
        link.read_link_handler, lambda c: c.data and c.data.startswith("read")
    )

    dp.register_message_handler(feedback.feedback_handler, commands="feedback")

    dp.register_message_handler(hour.hour_handler, commands="hour")

    dp.register_message_handler(mailing.mailing_handler, commands="admin_mailing")

    dp.register_message_handler(statistics.statistics_handler, commands="statistics")
    dp.register_message_handler(statistics.bot_statistics_handler, commands="botstatistics")
