import functools

from app import enums
from app.database.models import StatisticsRecord


def catch_intent(intent: enums.Intent):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            await StatisticsRecord.create(intent=intent)
            return await func(*args, **kwargs)

        return wrapper

    return decorator
