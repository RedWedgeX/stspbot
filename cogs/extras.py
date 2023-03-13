import nextcord as discord
from nextcord.ext import commands
from utils.helpers import openai_q_and_a, cgpt
from utils.config import *
import traceback
from revChatGPT.V1 import Chatbot

class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client


    @commands.command(hidden=True)
    @commands.has_any_role(staff, mods)
    async def cgpt(self, ctx, *query: str):
        async with ctx.typing():
            query = ' '.join(query)
            # query = ctx.message.content
            print(f"query: {query}")
            response = cgpt(query, ctx.message.author.id)
            await ctx.send(response)


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

    @commands.command()
    async def ama(self, ctx, *query: str):
        query = ' '.join(query)
        print(query)
        try:
            answer = openai_q_and_a(query)
            await ctx.send(f"{ctx.message.author.mention} asked: ```{query}```\n**Answer**: ```{answer}```")
        except Exception as e:
            await ctx.send(f"Sorry {ctx.message.author}, something went wrong.")
            print(e)

def setup(client):
    client.add_cog(Extras(client))
