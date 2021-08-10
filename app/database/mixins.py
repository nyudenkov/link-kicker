from tortoise import fields
from tortoise import models


class CreatedMixin(models.Model):
    dt_create = fields.DatetimeField(auto_now_add=True)


class UpdatedMixin(models.Model):
    dt_update = fields.DatetimeField(auto_now=True)


class ModelMixin(CreatedMixin, UpdatedMixin):
    pass
