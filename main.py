import json

import discord
import os
from discord.ext import commands

import SECRETS


def get_prefix(client, message):
    with open("./cogs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event
async def on_guild_join(guild):
    with open("./cogs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open("./cogs/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("./cogs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("./cogs/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def setprefix(ctx, prefix):
    with open("./cogs/prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("./cogs/prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(embed=discord.Embed(color=discord.Color.green(), title="Changed Prefix", description=f"Changed the prefix to **`{prefix}`**"))


@client.command()
async def reload(ctx):
    for ext in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.reload_extension(f"cogs.{ext[:3]}")
    await ctx.send(embed=discord.Embed(color=discord.Color.green(), title="Status", description="Reloaded extensions successful!"))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(SECRETS.TOKEN)
