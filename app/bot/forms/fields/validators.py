import sentry_sdk
from aiogram_forms.base import BaseValidator


class IntRangeValidator(BaseValidator):
    def __init__(self, start: int, end: int) -> None:
        self._start = start
        self._end = end
        super().__init__()

    async def validate(self, value: str) -> bool:
        try:
            value = int(value)
        except ValueError as ex:
            sentry_sdk.capture_exception(ex)
            return False
        return self._start <= value <= self._end
