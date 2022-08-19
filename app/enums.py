from enum import Enum


class Intent(str, Enum):
    RANDOM = "random"
    ADD = "add"
    DELETE = "delete"
    READ = "read"
    STATISTICS = "statistics"
    FEEDBACK = "feedback"
    HOUR = "hour"
    TIMEZONE = "timezone"
    LINKS = "links"
    LANGUAGE = "language"
    MAILING = "mailing"


class ReportType(str, Enum):
    BUG = "bug"
    FEATURE = "feature"
