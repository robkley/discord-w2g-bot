import os

import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("watchy"):
        headers = {
            'w2g_api_key': os.getenv("DISCORD_W2G_API_KEY"),
            'bg_color': '#000000',
            'bg_opacity': '100'
        }
        r = requests.post(url='https://api.w2g.tv/rooms/create.json', data=headers, timeout=10)
        response = r.json()
        w2g_room_url = "https://w2g.tv/de/room/?room_id=" + response['streamkey']
        await message.channel.send(f":white_check_mark: Ein neuer Watch2Gether-Raum wurde erfolgreich erstellt: {w2g_room_url}")


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

client.run(os.getenv("DISCORD_W2G_TOKEN"))
