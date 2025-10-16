from .input_media import InputMedia


class InputMediaDocument(InputMedia):

    def __init__(
            self,
            media: str = None,
            thumbnail: str = None,
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
