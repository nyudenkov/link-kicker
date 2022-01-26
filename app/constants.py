from typing import Any

from app.bot.middlewares import i18n

_ = i18n.gettext


class Constants:
    """
    A base class for defining a class with a set of constants.
    Implements property "all" to get all values of constants.
    The child class attributes must be set in upper case.
    """

    value_type: Any

    @classmethod
    def all(cls) -> tuple:
        keys = [
            key
            for key, value in cls.__dict__.items()
            if isinstance(value, cls.value_type) and key.isupper()
        ]
        return tuple([getattr(cls, key) for key in keys])


class StrConstants(Constants):
    """
    A base class for defining a class with a set of string constants.

    Examples
    --------
    >>> class ExampleClass(object, metaclass=StrConstants):
    ...     FIRST = 'first'
    ...     SECOND = 'second'
    ...     THIRD = 'third'
    ...
    >>> print(ExampleClass.all())
    ... ('first', 'second', 'third')
    >>> print(ExampleClass.FIRST)
    ... 'first'
    """

    value_type = str


class IntConstants(Constants):
    """
    A base class for defining a class with a set of integer constants.

    Examples
    --------
    >>> class ExampleClass(object, metaclass=IntConstants):
    ...     FIRST = 1
    ...     SECOND = 2
    ...     THIRD = 3
    ...
    >>> print(ExampleClass.all())
    ... (1, 2, 3)
    >>> print(ExampleClass.FIRST)
    ... 1
    """

    value_type = int


class Message(StrConstants):
    READ = _("🧐️ Прочитано")
    DELETE = _("🗑 Удалить")
    SAVED_LINK = _("🤘 Ссылку сохранил")
    NOTHING_TO_SEND = _("🍻 Все ссылочки уже прочитаны, мне нечего тебе отправить. Пополняй запасы :)")
    NOTHING_TO_SEND_MAILING = _("☹️ Мне тебе нечего отправлять в ежедневной рассылке! Давай-давай, закинь еще ссылочек\n\n➡️ Оставить отзыв: /feedback")
    LINK_DELETED = _("🗑 Ссылку удалил")
    LINK_WAS_READ = _("🤸‍♀️ Йоу, минус одна непрочитанная ссылка!")
    LINK_NOT_FOUND = _("🤔 Ссылок в сообщении не найдено")
    FEEDBACK = _("Хочешь оставить отзыв о работе бота?\nhttps://forms.gle/uCbnjoq746AJKKdr9")
    F_SAVED_LINKS_COUNT = _("🤘 Добавил ссылки из сообщения ({})")
    F_STATISTICS = _("📈 Твоя статистика:\nДобавлено ссылок: {}\nИз них прочитано (за все время): {} 🦾")
    F_BOT_STATISTICS = _("📈 Статистика бота:\nДобавлено ссылок: {}\nПрочитали: {}")
    F_URL = _("📤 {}")
    F_DELETE_URL = _("🗑 Удалить {}")
    F_URL_MAILING = _("📤 Привет! Твоя ссылочка почитать на сегодня: {}\n\n➡️ Оставить отзыв: /feedback")
    F_LINKS = _("Твои непрочитанные ссылки (страница {}):\n{}")
    F_LINK_ALREADY_WAS_ADDED = _("🥲 Ссылка {} уже добавлена")


class Regexp(StrConstants):
    LINK = "(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,10}(:[0-9]{1,5})?(\/.*)?"  # noqa
