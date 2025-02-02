import os

from flask import Flask, request, jsonify

from discord_interactions import verify_key_decorator, InteractionType, InteractionResponseType
from restaurant_club_bot.handler.interaction_handler import InteractionHandler

CLIENT_PUBLIC_KEY = os.getenv('PUBLIC_KEY')
if CLIENT_PUBLIC_KEY is None:
  print('noneeeee')

app = Flask(__name__)

"""
TODO
- Convert 'Headers' to dict with comma-separated values for multivalue headers
- 
"""

handler = InteractionHandler()

@app.route('/interactions', methods=['POST'])
@verify_key_decorator(CLIENT_PUBLIC_KEY)
def interactions():
  if request.json['type'] == InteractionType.APPLICATION_COMMAND:
    request.headers
    return jsonify(handler.hello_world())
  
