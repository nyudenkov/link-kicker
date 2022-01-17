import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger

from .jobs import link_mailing

__all__ = ["scheduler", "timedelta_trigger"]

scheduler = AsyncIOScheduler()
scheduler.add_job(
    link_mailing,
    CronTrigger(hour="*"),
)


def timedelta_trigger(td: datetime.timedelta):
    return DateTrigger(run_date=datetime.datetime.now() + td)
