import typing as t

from aiogram import types

from app.bot.middlewares import i18n
from app.constants import Message
from app.database.models import Link, User

_ = i18n.gettext


async def get_random_link_message(
    user: User, mailing: bool = False
) -> tuple[t.Optional[str], t.Optional[types.InlineKeyboardMarkup]]:
    if link := await Link.get_random_by_owner(user):
        markup = types.InlineKeyboardMarkup()
        markup.insert(
            types.InlineKeyboardButton(_(Message.READ), callback_data=f"read_{link.id}")
        )
        if mailing:
            return _(Message.F_URL_MAILING).format(link.url), markup
        return _(Message.F_URL).format(link.url), markup
    else:
        if mailing:
            return None, None
        return _(Message.NOTHING_TO_SEND), None
