from enum import auto

from .name_enum import NameEnum


class ChatMemberStatus(NameEnum):
    MEMBER = auto()
    ADMINISTRATOR = auto()
    CREATOR = auto()
    RESTRICTED = auto()
    LEFT = auto()
    BANNED = auto()
