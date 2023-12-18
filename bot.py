import discord
import os
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        await message.channel.send('Under Development')
    except Exception as e:
        pass

def run_discord_bot():
    load_dotenv()
    token = os.getenv('TOKEN')
    client = discord.Client(intents=discord.Intents.default())
    print(token)

    @client.event
    async def on_ready():
        print(f'Bot is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        await send_message(message, "", False)
        
    
    client.run(token)