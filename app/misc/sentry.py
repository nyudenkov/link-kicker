import sentry_sdk
from loguru import logger

from app import config


def init_sentry() -> None:
    if config.SENTRY_URL:
        logger.info("Initializing Sentry")
        sentry_sdk.init(config.SENTRY_URL, traces_sample_rate=1.0)


def capture_exception(exception: BaseException) -> None:
    logger.error(exception)
    sentry_sdk.capture_exception(exception)
