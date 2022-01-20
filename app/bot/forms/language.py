from aiogram import types
from aiogram_forms import fields
from aiogram_forms import forms

from app.bot import bot
from app.bot.forms import HourForm
from app.bot.forms import hour_form_callback
from app.bot.middlewares import i18n
from app.database.models import User

_ = i18n.gettext


class LanguageForm(forms.Form):
    languages = [language.label for language in i18n.AVAILABLE_LANGUAGES.values()]
    language_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True).add(*languages)
    language = fields.ChoicesField(
        label=_("Выбери язык"),
        choices=languages,
        reply_keyboard=language_keyboard
    )


async def language_form_callback():
    user, created = await User.get_or_create(tg_id=types.Chat.get_current().id)
    data = await LanguageForm.get_data()
    language = data["LanguageForm:language"]
    for lang_key, lang_data in i18n.AVAILABLE_LANGUAGES.items():
        if lang_data.label == language:
            user.language_iso = lang_key
            await user.save()
            i18n.ctx_locale.set(lang_key)
            await bot.send_message(
                chat_id=user.tg_id,
                text="👌"
            )
            return
    await bot.send_message(
        chat_id=user.tg_id,
        text="Something went wrong."
    )


async def start_language_form_callback():
    await language_form_callback()
    await HourForm.start(hour_form_callback)
