import asyncio

import discord
from discord.ext import commands


class Start(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is logged in successfully")

        while True:
            await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="the developers"))
            await asyncio.sleep(10)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="to .help"))
            await asyncio.sleep(10)


def setup(client):
    client.add_cog(Start(client))
