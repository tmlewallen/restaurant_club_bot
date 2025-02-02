import json
import os
from typing import Dict
from restaurant_club_bot.interaction.model.response import Response
from restaurant_club_bot.model.url_invocation import UrlInvocation
from discord_interactions import verify_key, InteractionType, InteractionResponseType


class InteractionHandler:

    def __init__(
        self, client_key: str = None, bot_token: str = None, app_id: str = None
    ):
        self._client_key = client_key if client_key else os.getenv("PUBLIC_KEY")
        self._bot_token = bot_token if bot_token else os.getenv("DISCORD_TOKEN")
        self._app_id = app_id if app_id else os.getenv("APP_ID")

    def handle_request(self, request: UrlInvocation) -> Response:
        if not self._is_interaction(request):
            return Response(status=404)
        if not self._authenticate(request):
            return Response(status=401)
        body = json.loads(request.body) if request.body else None
        if body and body.get("type") == InteractionType.PING:
            return Response(payload={"type": InteractionResponseType.PONG})
        else:
            return Response(
                payload={
                    "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                    "data": {"content": "Hello world"},
                }
            )

    def _is_interaction(self, request: UrlInvocation) -> bool:
        return (
            request.request_context.http.method == "POST"
            and request.request_context.http.path == "/interactions"
        )

    def _authenticate(self, request: UrlInvocation) -> bool:
        signature = request.headers.get("x-signature-ed25519")
        timestamp = request.headers.get("x-signature-timestamp")
        raw_body = request.body.encode("utf-8")
        return verify_key(raw_body, signature, timestamp, self._client_key)
