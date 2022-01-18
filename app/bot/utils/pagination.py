import typing as t
from math import ceil

from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from tortoise.queryset import QuerySet

from app import config


class QuerySetPaginationKeyboard(InlineKeyboardMarkup):
    handler_name: str
    data: list
    qs: QuerySet
    max_page: int
    count: int
    page: int

    def __init__(self, qs: QuerySet, handler_name: str, page: int = 1, count: int = config.PAGINATION_ITEMS_COUNT,
                 inline_keyboard=None, **kwargs):
        super(QuerySetPaginationKeyboard, self).__init__(row_width=2, inline_keyboard=inline_keyboard, **kwargs)
        self.qs = qs
        self.page = page
        self.count = count
        self.handler_name = handler_name + "_paginator"

    @property
    async def max_page(self) -> int:
        return ceil(await self.qs.count() / self.count)

    async def get_keyboard(self) -> t.Tuple["QuerySetPaginationKeyboard", t.List]:
        self.data = await self.qs.offset(0 if self.page == 1 else (self.count * (self.page - 1))).limit(self.count)
        if self.page != 1:
            self.insert(types.InlineKeyboardButton("◀️", callback_data=f"{self.handler_name}_{self.page - 1}"))
        if self.page != await self.max_page:
            self.insert(types.InlineKeyboardButton("▶️", callback_data=f"{self.handler_name}_{self.page + 1}"))
        self.row()
        return self, self.data
