import os
from typing import Dict
from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType



class InteractionHandler:

    def __init__(
        self, client_key: str = None, bot_token: str = None, app_id: str = None
    ):
        self._client_key = client_key if client_key else os.getenv("PUBLIC_KEY")
        self._bot_token = bot_token if bot_token else os.getenv("DISCORD_TOKEN")
        self._app_id = app_id if app_id else os.getenv("APP_ID")

    def hello_world(self) -> Dict:
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {"content": "Hello world, Rachel"},
        }
