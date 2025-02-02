import json
from restaurant_club_bot.interaction.interaction_handler import InteractionHandler
from restaurant_club_bot.model.url_invocation import UrlInvocation
from discord_interactions import verify_key

from discord_interactions import InteractionResponseType, InteractionType

handler = InteractionHandler()


def lambda_entry(event, context):
    url_invocation: UrlInvocation = UrlInvocation.from_dict(event)
    print(url_invocation)
    response = handler.handle_request(url_invocation)
    return {
        "statusCode": response.status,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(response.payload if response.payload else "{}"),
        "cookies": [],
        "isBase64Encoded": False,
    }
