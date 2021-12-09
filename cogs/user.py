import discord
from discord.ext import commands

from utils import helpers


# ###---Class for general/other commands---####
class User(commands.Cog, name="General User Commands"):
    def __init__(self, client):
        self.bot = client

    @commands.command(name='server')
    async def server(self, ctx):
        """ - Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=helpers.date(ctx.guild.created_at), inline=True)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)


def setup(client):
    client.add_cog(User(client))
