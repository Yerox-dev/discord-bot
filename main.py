import discord
import os
from discord.ext import commands

import SECRETS

client = commands.Bot(command_prefix=".")


@client.command()
async def reload(ctx):
    for ext in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.reload_extension(f"cogs.{ext[:3]}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(SECRETS.TOKEN)