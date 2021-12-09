from discord.ext import commands, tasks

from utils.config import staff

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


def setup(client):
    client.add_cog(SysAdmin(client))
