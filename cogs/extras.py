import discord
from discord.ext import commands
from utils.helpers import openai_q_and_a
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

    @commands.command()
    async def ama(self, ctx, *query: str):
        question = ' '.join(query)
        try:
            answer = openai_q_and_a(question)
            await ctx.send(f"{ctx.message.author.mention} asked: ```{question}```:\n**Answer**: ```{answer}````")
        except Exception as e:
            await ctx.send(f"Sorry {ctx.message.author}, something went wrong.")

def setup(client):
    client.add_cog(Extras(client))
