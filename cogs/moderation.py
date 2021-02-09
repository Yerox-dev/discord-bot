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

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        embed = discord.Embed(color=discord.Color.orange(), title=f":boom: Banned {member}",
                              description=f"{member} was banned from the Server :no_entry:\nReason: {reason}")
        if reason is None:
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), title="Missing Argument", description="You need to specify a reason!"))
            return
        if member == ctx.message.author:
            await ctx.send(embed=discord.Embed(color=discord.Color.red(), title="Error", description="You can't ban yourself"))
            return
        await ctx.send(embed=embed)
        await member.send(embed=embed)
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_user = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_user:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title=f"Unbanned {member}!",
                                      description=f"{user.mention} is now unbanned! :white_check_mark:",
                                      color=discord.Color.green())
                await ctx.send(embed=embed)
                return


def setup(client):
    client.add_cog(Moderation(client))
