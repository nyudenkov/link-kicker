from typing import Any

from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Format

from app.bot.dialogs import HourDialogSG
from app.bot.dialogs.widgets.text import IConst
from app.bot.middlewares import i18n
from app.database.models import User

_ = i18n.gettext
languages = {lang_data.label: lang for lang, lang_data in i18n.AVAILABLE_LANGUAGES.items()}


class LanguageDialogSG(StatesGroup):
    main = State()


async def on_lang_clicked(c: CallbackQuery, select: Any, manager: DialogManager, lang_label: str):
    user, created = await User.get_or_create(tg_id=c.from_user.id)
    context = manager.current_context()
    lang = languages[lang_label]
    i18n.ctx_locale.set(lang)
    await user.set_language(lang)
    await c.message.edit_text(_("👌 Успешно установлен {} язык").format(lang_label))
    await manager.done()

    if context.start_data:
        await manager.start(HourDialogSG.main, mode=StartMode.RESET_STACK)


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
        state=LanguageDialogSG.main,
    )
)
