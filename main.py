from aiogram import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_dialog import DialogRegistry
from loguru import logger
from tortoise import Tortoise

from app import commands
from app import config
from app.bot import bot
from app.bot import handlers
from app.bot import middlewares
from app.bot.dialogs import register_dialogs
from app.database import TORTOISE_ORM
from app.misc import set_commands
from app.misc.sentry import init_sentry
from app.tasks import scheduler

# Storage and dispatcher instances
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
registry = DialogRegistry(dp)


async def startup(dispatcher: Dispatcher):
    logger.info("Registering dialogs")
    await register_dialogs(registry)

    # Setup handlers
    logger.info("Configuring handlers...")
    handlers.setup(dispatcher)

    logger.info("Configuring Database")
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()

    # Set command hints
    await set_commands(dispatcher, commands)

    middlewares.setup(dispatcher)

    logger.info("Start scheduler")
    scheduler.start()

    init_sentry()

    logger.info("Start polling")


async def shutdown(dispatcher: Dispatcher):
    await Tortoise.close_connections()


if __name__ == "__main__":
    # Start long-polling mode
    executor.start_polling(
        dp, on_startup=startup, on_shutdown=shutdown, skip_updates=config.EXECUTOR_SKIP_UPDATES
    )
