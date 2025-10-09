from typing import Union

import balethon
from ...objects import Chat


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        return await self.auto_execute("post", "getChat", locals())
