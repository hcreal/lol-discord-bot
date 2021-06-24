import discord
from lol import main
TOKEN = "Token"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'lol!':
        msg = main()
        await message.channel.send(msg)
client.run(TOKEN)
