from typing import Dict

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.text.format import _FormatDataStub

from app.bot.middlewares import i18n

_ = i18n.gettext


class IConst(Const):
    async def _render_text(self, data: Dict, manager: DialogManager) -> str:
        return _(self.text)


class IFormat(Format):
    async def _render_text(self, data: Dict, manager: DialogManager) -> str:
        if manager.is_preview():
            return _(self.text.format_map(_FormatDataStub(data=data)))
        return _(self.text.format_map(manager.current_context().dialog_data | data))
