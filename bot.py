from discord.ext import commands
from summoners import summoners
from lol import main
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message(message):
    if "dornbob" in message.author.name:
        await message.channel.send("Nathan you're a filthy slut and I love it")
    if message.content == "hello":
        await message.channel.send("pies are better than cakes. change my mind.")

    await bot.process_commands(message)


@bot.command()
async def lol(ctx, summoner_name):
    if summoner_name in summoners.keys():
        summoner_name = summoners[summoner_name]
    msg = main(summoner_name)
    await ctx.channel.send(msg)

bot.run(os.environ["discord_api"])
