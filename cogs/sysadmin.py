import discord
from discord.ext import commands, tasks
from utils.config import *
from discord.errors import HTTPException
SUCCESS = '**`SUCCESS`**'
ERROR = '**`ERROR`**'


class SysAdmin(commands.Cog, name="Bot admin commands"):
    def __init__(self, client):
        self.bot = client
        self.healthcheck.start()

    def cog_unload(self):
        self.healthcheck.cancel()

    @tasks.loop(minutes=2)
    async def healthcheck(self):
        "foo"
        # requests.get("https://heartbeat.vuln.pw/ping/c6743519-5147-496e-91d9-eb68eece0bdd")

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.has_any_role(staff)
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'{ERROR} {type(e).__name__} - {e}')
        else:
            await ctx.send(SUCCESS)

    @commands.command(name='unload', hidden=True)
    @commands.has_any_role(staff)
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'{ERROR} {type(e).__name__} - {e}')
        else:
            await ctx.send(SUCCESS)

    @commands.command(name='reload', hidden=True)
    @commands.has_any_role(staff)
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'{ERROR} {type(e).__name__} - {e}')
        else:
            await ctx.send(SUCCESS)

    @commands.command(name='error', hidden=True)
    @commands.has_any_role(staff)
    async def error(self, ctx):
        raise ValueError('An error has been manually triggered for testing purposes.')

    @commands.command(name='roles')
    @commands.has_any_role(staff)
    async def reset_role_message(self, ctx):
        # Set up the reaction channel
        channel = self.bot.get_channel(ROLE_CHANNEL)
        try:
            await channel.purge(limit=10)
        except AttributeError as e:
            print(e)

        # DELETE AND CREATE ROLE CHANNEL MESSAGE
        role_list = ""

        for k, v in SELF_ASSIGN_ROLES.items():
            role = discord.utils.get(channel.guild.emojis, name=k)
            if role:
                role_list += f"{role}: {v}\n"
            else:
                role_list += f"{k}: {v}\n"

        role_message = f"{ROLES_CHANNEL_MESSAGE}\n{role_list}\n---------"
        msg = await channel.send(role_message)

        for k, v in SELF_ASSIGN_ROLES.items():
            try:
                await msg.add_reaction(k)
            except HTTPException:
                emoji = discord.utils.get(msg.guild.emojis, name=k)
                await msg.add_reaction(emoji)

            await ctx.send(SUCCESS)

def setup(client):
    client.add_cog(SysAdmin(client))
