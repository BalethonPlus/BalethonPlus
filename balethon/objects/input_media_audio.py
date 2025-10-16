from .input_media import InputMedia


class InputMediaAudio(InputMedia):

    def __init__(
            self,
            media: str = None,
            thumbnail: str = None,
            caption: str = None,
            duration: int = None,
            title: str = None,
            **kwargs
    ):
        super().__init__(
            type="audio",
            media=media,
            thumbnail=thumbnail,
            caption=caption,
            duration=duration,
            title=title,
            **kwargs
        )
