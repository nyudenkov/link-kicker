from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from tortoise import Tortoise

from app import config
from app.bot import bot
from app.bot import handlers
from app.misc import set_commands
from app.tasks import scheduler

# Storage and dispatcher instances
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def startup(dispatcher: Dispatcher):
    # Setup handlers
    logger.info("Configuring handlers...")
    handlers.setup(dispatcher)

    logger.info("Configuring Database")
    await Tortoise.init(
        db_url=f"sqlite://db.sqlite3", modules={"models": ["app.database.models"]}
    )
    await Tortoise.generate_schemas()

    # Set command hints
    await set_commands(dispatcher, config.get("commands"))

    logger.info("Start scheduler")
    scheduler.start()

    logger.info("Start polling")


async def shutdown(dispatcher: Dispatcher):
    await Tortoise.close_connections()


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(
        dp, on_startup=startup, on_shutdown=shutdown, **config.get("executor")
    )
