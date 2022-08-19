from aiogram_dialog import DialogRegistry

from .feedback import FeedbackDialogSG
from .feedback import feedback_dialog
from .hour import HourDialogSG
from .hour import hour_dialog
from .language import LanguageDialogSG
from .language import language_dialog
from .timezone import TimezoneDialogSG
from .timezone import timezone_dialog


async def register_dialogs(registry: DialogRegistry):
    registry.register(language_dialog)

    registry.register(feedback_dialog)

    registry.register(hour_dialog)
    registry.register(timezone_dialog)
