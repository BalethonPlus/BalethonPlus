from typing import Union

import balethon


class AskReview:

    async def ask_review(
            self: "balethon.Client",
            user_id: Union[int, str]
    ) -> bool:
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("post", "askReview", locals())
