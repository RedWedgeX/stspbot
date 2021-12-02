#!/usr/bin/python3

import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isfile, join



intents = discord.Intents.default()
intents.all()
intents.members = True

TOKEN = os.environ['TOKEN']

# FOR LOCAL TESTING
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cc9-discord-bots-8fd2dc16091f.json"

def get_prefix(bot, message):
    """A callable Prefix for our bot."""

    prefixes = ['!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, description='CactusCon Community Bot.', intents=intents)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    cogs_dir = 'cogs'
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            print(f"loading extension {extension}")
            bot.load_extension(cogs_dir + "." + extension)
        # except (discord.ClientException, commands.NoEntryPointError, ModuleNotFoundError):
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}.')

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Streaming(name='Say !help', url='https://cactuscon.com'))
    print(f'Successfully logged in and booted...!')


bot.run(TOKEN, bot=True, reconnect=True)