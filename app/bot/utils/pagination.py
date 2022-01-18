import typing as t

from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from tortoise.queryset import QuerySet


class QuerySetPaginationKeyboard(InlineKeyboardMarkup):
    handler_name: str
    data: list
    qs: QuerySet
    max_page: int
    count: int

    def __init__(self, qs: QuerySet, count: int, handler_name: str, inline_keyboard=None, **kwargs):
        super(QuerySetPaginationKeyboard, self).__init__(row_width=2, inline_keyboard=inline_keyboard, **kwargs)
        self.qs = qs
        self.count = count
        self.handler_name = handler_name + "_paginator"

    @property
    async def max_page(self) -> int:
        return await self.qs.count() // self.count

    async def get_keyboard(self, current_page: int) -> t.Tuple["QuerySetPaginationKeyboard", t.List]:
        self.data = await self.qs.limit(self.count).offset(self.count * current_page)
        if current_page != 1:
            self.insert(
                types.InlineKeyboardButton("◀️", callback_data=f"{self.handler_name}_{current_page-1}")
            )
        if current_page != await self.max_page:
            self.insert(
                types.InlineKeyboardButton("▶️", callback_data=f"{self.handler_name}_{current_page+1}")
            )
        return self, self.data
