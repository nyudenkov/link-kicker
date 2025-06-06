from typing import Any

from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified
from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.when import Whenable

from app.bot.dialogs.timezone import TimezoneDialogSG
from app.bot.dialogs.widgets.text import IConst
from app.bot.middlewares import i18n
from app.constants import welcome_text
from app.database.models import User

_ = i18n.gettext
languages = {
    lang_data.label: lang for lang, lang_data in i18n.AVAILABLE_LANGUAGES.items()
}


class LanguageDialogSG(StatesGroup):
    main = State()


async def on_lang_clicked(
    c: CallbackQuery, select: Any, manager: DialogManager, lang_label: str
):
    user, created = await User.get_or_create(tg_id=c.from_user.id)
    ctx = manager.current_context()
    lang = languages[lang_label]
    i18n.ctx_locale.set(lang)
    await user.set_language(lang)
    await c.message.edit_text(_("👌 Успешно установлен {} язык").format(lang_label))
    await manager.done()

    if ctx.start_data:
        try:
            await c.bot.edit_message_text(
                _(welcome_text), c.from_user.id, ctx.start_data["message_id"]
            )
        except MessageNotModified:
            pass
        await manager.start(
            TimezoneDialogSG.main, data=True, mode=StartMode.RESET_STACK
        )


def can_be_cancelled(data: dict, widget: Whenable, manager: DialogManager):
    return manager.current_context().start_data is None


language_dialog = Dialog(
    Window(
        IConst(_("Выбери язык")),
        Select(
            Format("{item}"),
            items=languages,
            item_id_getter=lambda x: x,
            id="lang",
            on_click=on_lang_clicked,
        ),
        Cancel(IConst(_("Отменить действие")), when=can_be_cancelled),
        state=LanguageDialogSG.main,
    )
)
