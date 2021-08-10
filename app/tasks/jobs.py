from app.bot import bot
from app.bot.messages import get_random_link_message
from app.database.models import User


async def link_mailing():
    for user in await User.all():
        message_text, markup = await get_random_link_message(user, mailing=True)
        await bot.send_message(user.tg_id, message_text, reply_markup=markup)
