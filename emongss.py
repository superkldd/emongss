import discord
import os
import requests
import asyncio
from json import loads



client = discord.Client()
embed = discord.Embed (title = '이곳을 눌러 바로 이동합니다.',
                       url = 'https://twitch.tv/mochapoo/ ',
                       description = "twitch/Mochapoo")
embed.set_image(url="https://images-ext-2.discordapp.net/external/Xeik7csyPXMo8ofWCvUU0rWOOgeuCK6CxHr5QoMLc0U/https/static-cdn.jtvnw.net/jtv_user_pictures/a04570df-723c-42b3-9d48-c39d898a40ee-profile_image-300x300.png")

embed2 = discord.Embed (title = '이곳을 눌러 바로 이동합니다.',
                       url = 'https://twitch.tv/emongss/ ',
                       description = "twitch/emongss")
embed2.set_image(url="https://images-ext-2.discordapp.net/external/19Ri2692b34cz0HZAVA_coyTp1_Nq4em_4-O_7HOWlY/https/static-cdn.jtvnw.net/jtv_user_pictures/15f113ea-23b5-4558-9951-202f53402bb2-profile_image-300x300.png")

embed3 = discord.Embed (title = '이곳을 눌러 바로 이동합니다.',
                       url = 'https://twitch.tv/ssozung/ ',
                       description = "twitch/ssozung")
embed3.set_image(url="https://images-ext-2.discordapp.net/external/dcEu0N9v-UW7qIavkGZCIq7c7NJ0jyEXlGKAZTw_7wg/https/static-cdn.jtvnw.net/jtv_user_pictures/0263e1f3-5648-42f8-9329-f56f41541470-profile_image-300x300.png")

embed4 = discord.Embed (title = '이곳을 눌러 바로 이동합니다.',
                       url = 'https://twitch.tv/eunjin2/ ',
                       description = "twitch/eunjin2")
embed4.set_image(url="https://images-ext-2.discordapp.net/external/3O0orPGJdQ8yoFMJCqXr8NyY-B2F8YGiJjQhLDe7KH4/https/static-cdn.jtvnw.net/jtv_user_pictures/6f8ba857-ae18-4458-8ffb-b8197256e197-profile_image-300x300.png")

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
                await channel.send(embed=embed2)
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)

@client.event
async def on_message(message):
    global msg
    if message.content.startswith('!모카푸'):
        await message.channel.send(embed=embed) 
        
    if message.content.startswith('!쏘정언니'):
        await message.channel.send(embed=embed3)
        
    if message.content.startswith('!은진언니'):
        await message.channel.send(embed=embed4)
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

