from aiogram_forms.base import BaseField

from app.bot.forms.fields.validators import IntRangeValidator

__all__ = ["IntRangeField"]


class IntRangeField(BaseField):
    def __init__(self, label: str, start: int, end: int, *args, **kwargs) -> None:
        super().__init__(label, *args, **kwargs)
        self._validators.append(IntRangeValidator(start, end))
