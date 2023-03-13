import nextcord as discord
from nextcord.ext import commands
from utils.config import *
import traceback

class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client


    @commands.command(hidden=True)
    @commands.has_any_role(staff, mods)
    async def cgpt(self, ctx, *query: str):
        async with ctx.typing():
            query = ' '.join(query)
            # query = ctx.message.content
            response = self.bot.chatbot.ask(convo_id=ctx.message.author.id, prompt=query)
            await ctx.send(response)


    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def script(self, ctx, movie):
        try:
            chanid =  918285694122721351
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
