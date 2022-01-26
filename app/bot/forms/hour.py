from aiogram import types
from aiogram_forms import forms

from app.bot import bot
from app.bot.forms.fields import IntRangeField
from app.bot.middlewares import i18n
from app.database.models import User

_ = i18n.gettext


class HourForm(forms.Form):
    hour = IntRangeField(
        label=_(
            "Напиши час во сколько тебе будет удобно получать ссылочку (по Московскому времени, надо написать цифру от 1 до 24)"
        ),
        start=1,
        end=24,
        validation_error_message=_("Тебе нужно написать цифру от 1 до 24")
    )


async def hour_form_callback():
    user, created = await User.get_or_create(tg_id=types.Chat.get_current().id)
    data = await HourForm.get_data()
    hour = int(data["HourForm:hour"])
    user.hour = hour
    await user.save()

    await bot.send_message(
        chat_id=user.tg_id,
        text=_(
            "Начнём? Отправляй любую ссылку в диалог и получишь ее в {}:00 по Московскому времени 👇🏻"
        ).format(hour) if created
        else _("Отправляй любую ссылку в диалог и получишь ее в {}:00 по Московскому времени 👇🏻").format(hour)
    )
