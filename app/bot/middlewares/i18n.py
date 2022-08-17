from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Optional
from typing import Tuple

from aiogram import types
from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from babel import Locale

from app.database.models import User


@dataclass
class LanguageData:
    flag: str
    title: str
    label: str = field(init=False, default=None)

    def __post_init__(self):
        self.label = f"{self.flag} {self.title}"


class I18nMiddleware(BaseI18nMiddleware):
    AVAILABLE_LANGUAGES = {
        "en": LanguageData("🇺🇸", "English"),
        "ru": LanguageData("🇷🇺", "Русский"),
    }

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        if isinstance(args[0], (types.Message, types.CallbackQuery)):
            user, _ = await User.get_or_create(tg_id=args[0].from_user.id)
            if user.language_iso:
                return user.language_iso

        tg_user: Optional[types.User] = types.User.get_current()
        locale: Optional[Locale] = tg_user.locale if tg_user else None
        if locale and locale.language in self.locales:
            *_, data = args
            language = data['locale'] = locale.language
            return language
        return self.default
