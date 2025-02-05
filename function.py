import os
import discord
from slack.errors import SlackApiError

# Initialize Slack client with OAuth token
discord_token = os.environ["discord_bot"]
discord_client = discord.Client()


AUTHORIZED_USER_IDS = ["frags230", "U23456789"]

# Function to handle message events
@discord_client.event
async def on_message(message):
    # Extract user ID and message content from the message
    user_id = str(message.author.id)
    message_content = message.content

    # Check if the user is authorized and the message contains the trigger phrase
    if message_content.lower() == "deactivate account" and user_id in AUTHORIZED_USER_IDS:
        response_message = "Hello! Your message was received and processed."
        await message.channel.send(response_message)
    else:
         # User is not authorized, send an error message
        error_message = "Sorry, you are not authorized to access this bot."
        await message.channel.send(error_message)
            
discord_client.run(discord_token)
