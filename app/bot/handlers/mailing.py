from aiogram import types

from app.bot import bot
from app.database.models import User


async def mailing_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    if user.tg_id != 956122347:  # TODO: Move id to config
        await message.reply("No access")
        return

    for user in await User.all():
        await bot.send_message(user.tg_id, message.text.removeprefix("/admin_mailing "))
