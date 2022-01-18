import re
from datetime import timedelta

from aiogram import types
from tortoise.transactions import in_transaction

from app import enums
from app.bot import utils
from app.bot.messages import get_random_link_message
from app.bot.utils.pagination import QuerySetPaginationKeyboard
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

    new_markup = callback_query.message.reply_markup
    if isinstance(new_markup.inline_keyboard[0], list):
        for idx_list, buttons_list in enumerate(new_markup.inline_keyboard):
            for idx, button in enumerate(buttons_list):
                if button.callback_data == callback_query.data:
                    new_markup.inline_keyboard[idx_list].pop(idx)
                    break
    else:
        new_markup = callback_query.message.reply_markup
        for idx, button in enumerate(new_markup.inline_keyboard):
            if button[0].callback_data == callback_query.data:
                new_markup.inline_keyboard.pop(idx)
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


async def render_links_message(data, page):
    return Message.F_LINKS.format(
        page, "\n".join([f"{idx}. {link.url}" for idx, link in enumerate(data, 1)])
    )


async def render_links_del_buttons(data, paginator):
    for idx, link in enumerate(data, 1):
        paginator.insert(
            types.InlineKeyboardButton(f"🗑 {idx}", callback_data=f"del_{link.id}")
        )
    return paginator


@utils.catch_intent(intent=enums.Intent.LINKS)
@utils.catch_error
async def links_handler(message: types.Message):
    user, created = await User.get_from_message(message)
    paginator, data = await (
        QuerySetPaginationKeyboard(await Link.get_unread_links_by_owner(user), 10, "links")
    ).get_keyboard(1)
    if data:
        reply_message = await render_links_message(data, 1)
        paginator = await render_links_del_buttons(data, paginator)
        await message.reply(reply_message, reply_markup=paginator, disable_web_page_preview=True)
        return
    await message.reply(Message.NOTHING_TO_SEND)


@utils.catch_error
async def links_page_handler(callback_query: types.CallbackQuery):
    user, created = await User.get_or_create(tg_id=callback_query.from_user.id)
    page = int(callback_query.data.removeprefix("links_paginator_"))
    paginator, data = await (
        QuerySetPaginationKeyboard(await Link.get_unread_links_by_owner(user), 10, "links")
    ).get_keyboard(page)
    reply_message = await render_links_message(data, page)
    paginator = await render_links_del_buttons(data, paginator)
    await callback_query.message.edit_text(reply_message, reply_markup=paginator, disable_web_page_preview=True)
