#!/usr/bin/python3

import os
from os import listdir
from os.path import isfile, join
from utils.config import CGPT_PROMPT
import nextcord as discord
from revChatGPT.V3 import Chatbot
from nextcord.errors import HTTPException
from nextcord.ext import commands

from utils.config import ROLE_CHANNEL, ROLES_CHANNEL_MESSAGE, SELF_ASSIGN_ROLES

intents = discord.Intents.default()
intents.all()
intents.message_content = True
intents.members = True

TOKEN = os.environ['TOKEN']


def get_prefix(bot, message):
    """A callable Prefix for our bot."""

    prefixes = ['!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# bot = commands.Bot(command_prefix=get_prefix, description='Gronp Bot.', intents=intents)

bot = commands.Bot(command_prefix="!", description='Gronp Bot.', intents=intents)

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    cogs_dir = 'cogs'
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            print(f"loading extension {extension}")
            bot.load_extension(cogs_dir + "." + extension)
        # except (discord.ClientException, commands.NoEntryPointError, ModuleNotFoundError):
        except Exception as e:
            raise e
            print(f'Failed to load extension {extension}: {e}.')


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(
        activity=discord.Streaming(name='Dom Jot', url='https://www.facebook.com/groups/1477972915840370'))
    bot.chatbot = Chatbot(api_key=os.environ['CHATGPT_API'], system_prompt=CGPT_PROMPT)
    bot.cgpt_enabled = True
    print(f'Successfully logged in and booted...!')


bot.run(TOKEN, reconnect=True)
