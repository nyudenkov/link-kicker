from typing import Dict

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Const

from app.bot.middlewares import i18n

_ = i18n.gettext


class IConst(Const):
    async def _render_text(self, data: Dict, manager: DialogManager) -> str:
        return _(self.text)
