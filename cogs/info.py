import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed=discord.Embed(color=discord.Color.green(), title="Pong!",
                                           description=f"Your ping is {round(self.client.latency * 1000)}ms :stopwatch:"))


def setup(client):
    client.add_cog(Info(client))
