import discord
import asyncio
import requests


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    game = discord.Game("열심히")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "emogss"
    name = "에몽언니"
    channel = client.get_channel(404964728213995521)
    a = 0
    while True:
        headers = {'Client-ID': 'd3w46tya3886tar4s31enx8f9ya91p'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send("```" + name + " 님이 방송을 시작하였습니다." + "```")
                a = 1
        except:
            a = 0
        await asyncio.sleep(3)


client.run('NjI2MDgzMzY5OTE4Mzk4NTA0.XYo8-g.4GM7HCQwZkbL90KuN7hf9dpx41s')

