from os import environ

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = environ.get("BOT_TOKEN")
ADMIN_CHAT_ID = int(environ.get("ADMIN_CHAT_ID"))

SENTRY_URL = environ.get("SENTRY_URL")

DATABASE_URL = environ.get("DATABASE_URL")

REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")

EXECUTOR_SKIP_UPDATES = environ.get("EXECUTOR_SKIP_UPDATES", True)

PAGINATION_ITEMS_COUNT = int(environ.get("BOT_PAGINATION_ITEMS_COUNT", 10))
