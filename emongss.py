import discord
import os
import requests
import asyncio
from json import loads



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("열심히")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "emongss"
    name = "에몽언니"
    channel = client.get_channel(404964728213995521)
    a = 0
    while True:
        headers = {'Client-ID': 'v2n7lbn2edlcaylh0qzcjtrhwws025'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("```" + name + " 가 방송을 시작했다 !!! " + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

