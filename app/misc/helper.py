from aiogram import Dispatcher
from aiogram.types import BotCommand
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


async def set_commands(dp: Dispatcher, commands: dict):
    """
    Set command hints
    """
    for lang_code, descriptions in commands.items():
        await dp.bot.set_my_commands(
            [
                BotCommand(command, description)
                for command, description in descriptions.items()
            ],
            language_code=lang_code,
        )


def parse_config(path):
    """
    Parse a config
    """

    with open(path) as file:
        return load(file, Loader=Loader)
