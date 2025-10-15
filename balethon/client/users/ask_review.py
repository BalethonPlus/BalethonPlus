import balethon


class AskReview:

    async def ask_review(
            self: "balethon.Client",
            user_id: int
    ) -> bool:
        return await self.auto_execute("post", "askReview", locals())
