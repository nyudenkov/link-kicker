import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from .jobs import link_mailing

__all__ = ["scheduler"]

scheduler = AsyncIOScheduler()
scheduler.add_job(
    link_mailing,
    CronTrigger(day="*", hour="19", timezone=pytz.timezone("Europe/Moscow")),
)
