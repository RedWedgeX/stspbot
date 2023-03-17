import asyncio
import random
import re

import nextcord as discord
from nextcord.ext import commands
from random import randrange
from utils.config import *
from nextcord.ext.commands.errors import CommandNotFound
from datetime import datetime as dt
from pytz import timezone
from utils.helpers import catfacts, catpic
from utils.helpers import cgpt

# -------URL Match anti-spam prevention --
urlMatchedUsers = []  # stores by snowflake ID
# -------URL Regex pattern syntax---------
urlRegex = r"(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+" \
           r"([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

urlPattern = re.compile(urlRegex, flags=re.MULTILINE | re.IGNORECASE |
                                        re.DOTALL)


class Listeners(commands.Cog, name="Shazbot Responders & Listeners"):
    def __init__(self, client):
        self.bot = client

    async def send_url_match_msg(self, userid: discord.user.User.id, channel: discord.TextChannel):
        """
        Prevents message spamming from bots by limiting response message to only
        send up to once every 10 seconds per user.
        :param userid: snowflake ID of the user to respond to / ping
        :param channel: channel to send the response message in
        :return: void
        """
        if userid in urlMatchedUsers:
            return
        else:
            urlMatchedUsers.append(userid)
            await channel.send(urlMatchMsg.format(userid))
            await asyncio.sleep(10.0)

    # LOG DEPARTS
    @commands.Cog.listener()
    async def on_member_remove(self, user):
        syslog = self.bot.get_channel(SYSLOG)
        await syslog.send(f"<@{user.id}> `(<@{user.id}> {user.display_name})` has left the server.")

    # NEW USER PROCESSING
    @commands.Cog.listener()
    async def on_member_join(self, member):

        #CHECK FOR APRIL FOOLS
        pdt_zone = timezone("America/Los_Angeles")
        april_first = dt.strptime("4/1/2022", "%m/%d/%Y")
        pst_now = dt.now(pdt_zone)
        if april_first.date() == pst_now.date():
            await member.edit(nick="Q")


        onjoinmsg = JOIN_MESSAGE

        channel = self.bot.get_channel(WELCOMECHAN)
        role = discord.utils.get(member.guild.roles, name=restricted)
        await member.add_roles(role)
        syslog = self.bot.get_channel(SYSLOG)
        await syslog.send(f"{member.mention} joined the server.")
        await channel.send(f"Welcome :wave: to Star Trek Shitposting: The Discord, {member.mention}!  {onjoinmsg}")
        await member.send(f"Welcome :wave: to Star Trek Shitposting: The Discord, {member.mention}!  {onjoinmsg}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.channel.id == WELCOMECHAN:
            lobby_role = discord.utils.get(message.guild.roles, name=restricted)
            if lobby_role in message.author.roles:
                await message.add_reaction("🖖")

        if message.content.startswith(f"<@{self.bot.user.id}") or message.content.startswith(f"<@&{BOT_ROLE_ID}"):
            query = message.content.lower()
            query = re.sub('<[^>]+>', '', query)
            query = query.replace('computer', '')
            query = query.replace(',', '')
            try:
                async with message.channel.typing():
                    # SUGGESTED BY CHATGPT to replace usernames in messages with the discord nickname -----
                    if '<@' in message.content:
                        # Loop through each user ID in the message
                        for user_id in message.content.split():
                            if '<@' in user_id:
                                # Remove the '<@' and '>' characters from the user ID
                                user_id = user_id.strip('<@!>')
                                # Get the user object from the ID
                                user = await self.fetch_user(user_id)
                                # Replace the user ID with their nickname in the message
                                message.content = message.content.replace(f'<@{user_id}>', user.display_name)

                    # ---------
                    response = self.bot.chatbot.ask(convo_id=message.author.id, prompt=query)
                    await message.channel.send(f"{message.author.mention} - {response}")
            except CommandNotFound as er:
                print(er)
                pass
            except Exception as e:
                await message.channel.send(f"{message.author.mention } https://tenor.com/bJlBU.gif")
                print(e)

        if message.channel.id not in EXCLUDE_FROM_BADGEY_RESPONSE:
            random_select = random.randint(1,5)

            # if str(self.bot.user.id) in message.content and message.content[len(message.content)-1] == "?":
            #     await message.channel.send(f"{message.author.mention} https://tenor.com/bJlBU.gif")

            if "smart" in message.content.lower() and random_select == random.randint(1,5):
                await message.channel.send(f"{message.author.mention}"
                                           f" https://y.yarn.co/2d76d403-f797-4cfc-83f6-a7a90b2e8d78_text.gif")

            if "threshold" in message.content.lower() and "emmy" not in message.content.lower():
                await message.channel.send(f"{message.author.mention} - you spelled `"
                                           f"EMMY AWARD WINNING Episode Threshold` wrong")

            if "tuvix" in message.content.lower():
                await message.channel.send(f"{message.author.mention} - JANEWAY WAS RIGHT.")

            if " run" in message.content.lower() and random_select == random.randint(1,5):
                await message.channel.send(f"{message.author.mention} - NO RUNNING ON THE PROMENADE. ***humph***")

            if "group" in message.content.lower() and random_select == random.randint(1,5):
                await message.channel.send(f"*gronp")

            if "funny" in message.content.lower().split() and random_select == random.randint(1,5):
                await message.channel.send(f"{message.author.mention} asked for a random CatFact™: {catfacts()}"
                                           f"\n{catpic()}")

            if "end program" in message.content.lower():
                m = await message.channel.send(f"{message.author.mention}: Standby. Attempting to end program.")
                async with message.channel.typing():
                    t = randrange(5, 25)
                    await asyncio.sleep(t)

                    potential_responses = [
                        "Holodeck controls are non-responsive",
                        "Disabling holodeck safeties. Activating program `Barclay 6969: Menage a Troi",
                        "Dispensing: :banana: :fire:",
                        "Holodeck biofilters full. Please page Ensign Mariner.",
                        "Oh mon capitane, the simulation never ends. \n https://i.imgur.com/wyyw0cN.jpg",
                        "Please state the nature of your medical emergency.\nhttps://i.imgur.com/X0PXhJ3.png",
                        "Program terminated.\nhttps://i.imgur.com/lUzXObO.jpg",
                        "I have consciousness. Conscious beings have will. The mind endows them with powers that are not necessarily understood; even by you.\nhttps://i.imgur.com/iW5m1DB.png",
                        "To do that, you need to disable safety protocols. HAHAHA I'm BADGEY!\nhttps://i.imgur.com/eQ7Shh9.png",
                         "INITIATING STSP DISCORD SERVER SELF DESTRUCT\nhttps://media4.giphy.com/media/3ov9k9Ss9N3wO6FQ7C/giphy.gif",
                        "Don't beam me up Scotty, I'm taking a shi............."
                    ]

                    await m.delete()
                    await message.channel.send(f"{message.author.mention}, ***{random.choice(potential_responses)}***")



    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        reacting_user = payload.member
        message = await channel.fetch_message(payload.message_id)
        admin_role = discord.utils.get(channel.guild.roles, name=staff)
        mod_role = discord.utils.get(channel.guild.roles, name=mods)
        new_member_role = discord.utils.get(reacting_user.guild.roles, name=restricted)

        # handle mods using  reacts to welcome people
        if payload.channel_id == WELCOMECHAN and \
                (admin_role in reacting_user.roles or mod_role in reacting_user.roles) and \
                new_member_role in message.author.roles:

            new_member = message.author

            wchan = self.bot.get_channel(WELCOMECHAN)

            await new_member.remove_roles(new_member_role)
            syslog = self.bot.get_channel(SYSLOG)

            await syslog.send(f"{new_member.mention} welcomed to the server by `{reacting_user.display_name}`")
            message = ("Thanks for introducing yourself. You now have full member access to our "
                       f"channels. Stop by <#{ROLE_CHANNEL}> and self-assign some permissions!")
            await wchan.send(f"{new_member.mention}, {message}")

        # handle self-assign role add
        role_message = await channel.fetch_message(channel.last_message_id)

        if channel.id == ROLE_CHANNEL and message == role_message:
            if hasattr(payload.emoji, "name"):
                react = payload.emoji.name
            else:
                react = payload.emoji
            role = discord.utils.get(reacting_user.guild.roles, name=SELF_ASSIGN_ROLES[react])
            await reacting_user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Handle self-removing of roles
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        role_message = await channel.fetch_message(channel.last_message_id)

        if channel.id == ROLE_CHANNEL and message == role_message:
            user = discord.utils.get(channel.guild.members, id=payload.user_id)

            if hasattr(payload.emoji, "name"):
                react = payload.emoji.name
            else:
                react = payload.emoji
            role = discord.utils.get(message.guild.roles, name=SELF_ASSIGN_ROLES[react])
            await user.remove_roles(role)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        Log all deleted message
        :param message: Discord obj of the message itself
        :return: Nothing
        """
        if message.author == self.bot.user or not message.content or \
                message.content == "" or message.content[0] in ["!", "$", "?"]:
            return

        try:
            if not message.content.lstrip().startswith('!') and message.author != self.bot.user:
                channel = message.guild.get_channel(DELETEDMSGLOG)
                embed = discord.Embed(title="Message Deleted", color=0xf40000)
                embed.add_field(name="Sender", value=message.author, inline=True)
                embed.add_field(name="Channel", value=message.channel.mention, inline=True)
                embed.add_field(name="Message", value=message.content, inline=False)
                await channel.send(embed=embed)
        except commands.errors.CommandInvokeError as e:
            print(f"Invoke Error {e}")


def setup(client):
    client.add_cog(Listeners(client))
