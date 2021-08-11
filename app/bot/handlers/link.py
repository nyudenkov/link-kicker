from aiogram import types

from app import enums
from app.bot.messages import get_random_link_message
from app.bot.utils.statistics import catch_intent
from app.constants import Message
from app.database.models import Link
from app.database.models import User


@catch_intent(intent=enums.Intent.ADD)
async def link_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    link: Link = await Link.create(url=message.text, owner=user)

    markup = types.InlineKeyboardMarkup()
    markup.insert(
        types.InlineKeyboardButton(Message.CANCEL, callback_data=f"del_{link.id}")
    )
    await message.reply(Message.SAVED_LINK, reply_markup=markup)


@catch_intent(intent=enums.Intent.RANDOM)
async def get_random_link_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    message_text, markup = await get_random_link_message(user)
    await message.reply(message_text, reply_markup=markup)


@catch_intent(intent=enums.Intent.DELETE)
async def del_link_handler(callback_query: types.CallbackQuery):
    user, created = await User.get_or_create(tg_id=callback_query.from_user.id)
    link: Link = await Link.get(id=callback_query.data.removeprefix("del_"), owner=user)
    await link.delete()
    await callback_query.message.delete_reply_markup()
    await callback_query.message.reply(Message.LINK_DELETED)


@catch_intent(intent=enums.Intent.READ)
async def read_link_handler(callback_query: types.CallbackQuery):
    user, created = await User.get_or_create(tg_id=callback_query.from_user.id)
    link: Link = await Link.get(
        id=callback_query.data.removeprefix("read_"), owner=user
    )
    link.was_read = True
    await link.save()
    await callback_query.message.delete_reply_markup()
    await callback_query.message.reply(Message.LINK_WAS_READ)
