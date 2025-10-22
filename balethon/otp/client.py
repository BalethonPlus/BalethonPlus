from time import time
from random import randint

from httpx import AsyncClient
from httpx._config import DEFAULT_TIMEOUT_CONFIG
from httpx._types import ProxyTypes, TimeoutTypes

from ..errors import RPCError
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class Client:
    BASE_URL = "https://safir.bale.ai"

    def __init__(
            self,
            id: str,
            secret: str,
            time_out: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
            proxy: ProxyTypes = None
    ):
        self.id = id
        self.secret = secret
        self.time_out = time_out
        self.proxy = proxy
        self.client = AsyncClient(proxy=self.proxy, timeout=self.time_out)
        self.__last_access_token = None
        self.__last_access_token_type = None
        self.__last_access_token_expire_time = None

    def __repr__(self):
        return f"{type(self).__name__}({self.id})"

    async def connect(self):
        return

    async def disconnect(self):
        await self.client.aclose()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.disconnect()

    async def get_access_token(self) -> tuple[str, str]:
        current_time = int(time())

        if (
            self.__last_access_token is not None
            and self.__last_access_token_type is not None
            and self.__last_access_token_expire_time - current_time > 60
        ):
            return self.__last_access_token, self.__last_access_token_type

        response = await self.client.post(
            f"{self.BASE_URL}/api/v2/auth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            params={
                "grant_type": "client_credentials",
                "client_secret": self.secret,
                "scope": "read",
                "client_id": self.id
            }
        )

        response_json = response.json()

        if response.status_code != 200:
            raise RPCError.create(response.status_code, response_json)

        self.__last_access_token = response_json["access_token"]
        self.__last_access_token_type = response_json["token_type"]
        self.__last_access_token_expire_time = current_time + response_json.get("expires_in", 43200)

        return self.__last_access_token, self.__last_access_token_type

    async def send_otp(self, phone: str, otp: int):
        token, token_type = await self.get_access_token()

        json = locals()
        del json["self"]

        response = await self.client.post(
            f"{self.BASE_URL}/api/v2/send_otp",
            headers={
                "Authorization": f"{token_type} {token}",
                "Content-Type": "application/json"
            },
            json=json
        )

        response_json = response.json()

        if response.status_code != 200:
            description = response_json.get("message")
            raise RPCError.create(
                response.status_code,
                description.capitalize() if description else description,
                "send_otp"
            )

    @staticmethod
    def passcode_generate(digits: int = 5) -> int:
        return int("".join(str(randint(1, 9)) for _ in range(digits)))
