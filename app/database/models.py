import typing as t
from random import choice

from aiogram import types
from tortoise import fields

from app import enums
from app.database import mixins

__all__ = ["User", "Link", "StatisticsRecord"]


class User(mixins.ModelMixin):
    id = fields.IntField(pk=True)
    tg_id = fields.IntField(unique=True)
    hour = fields.SmallIntField(null=True)

    links: fields.ReverseRelation["Link"]

    @classmethod
    async def get_from_message(cls, message: types.Message) -> t.Tuple["User", bool]:
        return await cls.get_or_create(tg_id=message.from_user.id)


class Link(mixins.ModelMixin):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=1024)
    was_read = fields.BooleanField(default=False)

    owner = fields.ForeignKeyField("models.User", related_name="links")

    # TODO: Add UUID4 field

    @classmethod
    async def get_random_by_owner(cls, owner: User) -> t.Optional["Link"]:
        link_ids: t.List[int] = await Link.filter(
            owner=owner, was_read=False
        ).values_list("id", flat=True)
        if link_ids:
            return await cls.get(id=choice(link_ids))
        return None

    @classmethod
    async def get_unread_links_by_owner(cls, owner: User) -> t.Optional[t.List["Link"]]:
        return await cls.filter(owner=owner, was_read=False)


class StatisticsRecord(mixins.CreatedMixin):
    intent = fields.CharEnumField(enums.Intent)
