from aiogram_dialog import DialogRegistry

from .hour import HourDialogSG
from .hour import hour_dialog
from .language import LanguageDialogSG
from .language import language_dialog
from .timezone import TimezoneDialogSG
from .timezone import timezone_dialog


async def register_dialogs(registry: DialogRegistry):
    registry.register(language_dialog)

    registry.register(hour_dialog)
    registry.register(timezone_dialog)
