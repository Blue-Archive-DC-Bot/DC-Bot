import discord
import os
from dotenv import load_dotenv
from response import get_response

COMMAND_PREFIX = "!"


async def send_message(channel, response_content, files):
    try:
        await channel.send(content=response_content, files=files)
    except Exception as e:
        print(e)
        pass


def setup_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    return intents


def run_discord_bot():
    load_dotenv()
    token = os.getenv("TOKEN")
    intents = setup_intents()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Bot is now running")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        print(f"content: {message.content}")

        if not message.content.startswith(COMMAND_PREFIX):
            return

        content = message.content[1:]
        response_content, files = get_response(content)

        await send_message(message.channel, response_content, files)

    client.run(token)
