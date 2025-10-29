from enum import auto

from .name_enum import NameEnum


class ChatAction(NameEnum):
    TYPING = auto()
    UPLOAD_PHOTO = auto()
    RECORD_VIDEO = auto()
    UPLOAD_VIDEO = auto()
    CHOOSE_STICKER = auto()
    RECORD_VOICE = auto()
    UPLOAD_VOICE = auto()
