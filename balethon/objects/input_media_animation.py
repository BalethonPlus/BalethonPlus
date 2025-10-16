from typing import Union, BinaryIO

from .input_media import InputMedia


class InputMediaAnimation(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BinaryIO] = None,
            thumbnail: str = None,
            caption: str = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            **kwargs
    ):
        super().__init__(
            type="animation",
            media=media,
            thumbnail=thumbnail,
            caption=caption,
            width=width,
            height=height,
            duration=duration,
            **kwargs
        )
