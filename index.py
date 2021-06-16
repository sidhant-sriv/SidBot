from configuration import config
import discord 
import os
from discord.ext import commands
client = commands.Bot(command_prefix="|")

@client.command()
async def load(ctx,extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        

@client.event
async def on_ready():
    print("Bot is ready")
client.run(config["discord-token"])
