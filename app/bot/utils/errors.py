import functools

from aiogram import types

from app.bot import bot
from app.misc.sentry import capture_exception


def catch_error(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as ex:
            capture_exception(ex)
            msg, chat_id = args[0], 0
            if type(msg) == types.CallbackQuery:
                chat_id = msg.message.chat.id
            elif type(msg) == types.Message:
                chat_id = msg.chat.id
            await bot.send_message(chat_id, "Возникла ошибка, сообщите @nyudenkov, пожалуйста")
    return wrapper
