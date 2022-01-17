import re
from datetime import timedelta

from aiogram import types
from tortoise.transactions import in_transaction

from app import enums
from app.bot.messages import get_random_link_message
from app.bot import utils
from app.constants import Message
from app.constants import Regexp
from app.database.models import Link
from app.database.models import User
from app.tasks import scheduler
from app.tasks import timedelta_trigger
from app.tasks.jobs import delete_message


@utils.catch_intent(intent=enums.Intent.ADD)
@utils.catch_error
async def link_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    link: Link = await Link.create(url=message.text, owner=user)

    markup = types.InlineKeyboardMarkup()
    markup.insert(
        types.InlineKeyboardButton(Message.DELETE, callback_data=f"del_{link.id}")
    )
    await message.reply(Message.SAVED_LINK, reply_markup=markup)


@utils.catch_intent(intent=enums.Intent.ADD)
@utils.catch_error
async def message_link_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    markup = types.InlineKeyboardMarkup(row_width=1)
    links_count = 0
    async with in_transaction():
        for url in re.finditer(Regexp.LINK, message.text):
            link = await Link.create(url=url.group(), owner=user)
            markup.insert(
                types.InlineKeyboardButton(Message.F_DELETE_URL.format(link.url), callback_data=f"del_{link.id}")
            )
            links_count += 1
    if links_count == 1:
        await message.reply(Message.SAVED_LINK, reply_markup=markup)
    elif links_count > 1:
        await message.reply(Message.F_SAVED_LINKS_COUNT.format(links_count), reply_markup=markup)
    else:
        await message.reply(Message.LINK_NOT_FOUND)


@utils.catch_intent(intent=enums.Intent.RANDOM)
@utils.catch_error
async def get_random_link_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    message_text, markup = await get_random_link_message(user)
    await message.reply(message_text, reply_markup=markup)


@utils.catch_intent(intent=enums.Intent.DELETE)
@utils.catch_error
async def del_link_handler(callback_query: types.CallbackQuery):
    user, created = await User.get_or_create(tg_id=callback_query.from_user.id)
    link: Link = await Link.get(id=callback_query.data.removeprefix("del_"), owner=user)
    await link.delete()

    keyboard_len = len(callback_query.message.reply_markup.inline_keyboard)
    if keyboard_len == 1:
        await callback_query.message.delete()
    elif keyboard_len > 1:
        new_markup = callback_query.message.reply_markup
        for count, button in enumerate(new_markup.inline_keyboard):
            if button[0].callback_data == callback_query.data:
                new_markup.inline_keyboard.pop(count)
                break
        await callback_query.message.edit_reply_markup(new_markup)
    sent = await callback_query.message.answer(Message.LINK_DELETED)
    scheduler.add_job(delete_message, timedelta_trigger(timedelta(seconds=3)), (sent.chat.id, sent.message_id))


@utils.catch_intent(intent=enums.Intent.READ)
@utils.catch_error
async def read_link_handler(callback_query: types.CallbackQuery):
    user, created = await User.get_or_create(tg_id=callback_query.from_user.id)
    link: Link = await Link.get(
        id=callback_query.data.removeprefix("read_"), owner=user
    )
    link.was_read = True
    await link.save()
    await callback_query.message.delete_reply_markup()
    await callback_query.message.reply(Message.LINK_WAS_READ)


@utils.catch_intent(intent=enums.Intent.LINKS)
@utils.catch_error
async def links_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    links = await Link.get_unread_links_by_owner(user)
    if links:
        reply_message = Message.F_LINKS.format(
            "\n".join([f"{idx}. {link.url}" for idx, link in enumerate(links)])
        )
        await message.reply(reply_message)
        return
    await message.reply(Message.NOTHING_TO_SEND)
