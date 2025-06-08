from aiogram_dialog import DialogRegistry

from .feedback import FeedbackDialogSG, feedback_dialog
from .hour import HourDialogSG, hour_dialog
from .language import LanguageDialogSG, language_dialog
from .timezone import TimezoneDialogSG, timezone_dialog

__all__ = [
    "FeedbackDialogSG",
    "feedback_dialog",
    "HourDialogSG",
    "hour_dialog",
    "LanguageDialogSG",
    "language_dialog",
    "TimezoneDialogSG",
    "timezone_dialog",
    "register_dialogs",
]


async def register_dialogs(registry: DialogRegistry):
    registry.register(language_dialog)

    registry.register(feedback_dialog)

    registry.register(hour_dialog)
    registry.register(timezone_dialog)
