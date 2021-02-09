import discord
from discord.ext import commands


class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print("DEBUG: Command " + ctx.command.name + " completed successfully")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), title="Can't found command!", description="The command is not valid!"))


def setup(client):
    client.add_cog(Event(client))
