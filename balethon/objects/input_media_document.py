from typing import Union, BinaryIO

from .input_media import InputMedia


class InputMediaDocument(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BinaryIO] = None,
            thumbnail: Union[str, bytes, BinaryIO] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__(
            type="document",
            media=media,
            thumbnail=thumbnail,
            caption=caption,
            **kwargs
        )
