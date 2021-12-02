import discord
from discord.ext import commands
from utils.config import *
from utils import helpers


# ###---Class for general/other commands---####
class Roles(commands.Cog, name="Stuff for self-assigning roles"):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def foo(self, ctx):
        "bar"



def setup(client):
    client.add_cog(Roles(client))
