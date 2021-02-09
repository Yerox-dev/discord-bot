import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(color=discord.Color.orange(), title=f"Kicked {member}",
                              description=f"{member} was kicked successfully. :x:")
        await ctx.send(embed=embed)
        await member.send(embed=embed)
        await member.kick(reason=reason)


def setup(client):
    client.add_cog(Moderation(client))
