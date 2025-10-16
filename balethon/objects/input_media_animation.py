from .input_media import InputMedia


class InputMediaAnimation(InputMedia):

    def __init__(
            self,
            media: str = None,
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
