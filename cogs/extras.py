import discord
from discord.ext import commands
from utils.config import *
import traceback

class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client

    # SCRIPT PLAYING
    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def script(self, ctx, movie):
        try:
            chanid=  918285694122721351
            chan = self.bot.get_channel(int(chanid))
            await ctx.send(f"connecting to {chan.name}")
            vc = await chan.connect()

            vc.play(discord.FFmpegPCMAudio(f'scripts/{movie}.mp3'))
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send

def setup(client):
    client.add_cog(Extras(client))
