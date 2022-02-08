import asyncio
import re

import discord
from discord.errors import HTTPException
from discord.ext import commands
from random import randrange
from utils.config import *

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

        if "threshold" in message.content.lower() and "emmy" not in message.content.lower():
            await message.channel.send(f"{message.author.mention} - you spelled `"
                                       f"EMMY AWARD WINNING Episode Threshold` wrong")

        if "tuvix" in message.content.lower():
            await message.channel.send(f"{message.author.mention} - JANEWAY WAS RIGHT.")
                      
        if " run" in message.content.lower():
            await message.channel.send(f"{message.author.mention} - NO RUNNING ON THE PROMENADE. ***humph***")

        if "group" in message.content.lower():
            await message.channel.send(f"*gronp")
                      
        if "even the" in message.content.lower():
            m = message.content.lower()
            m = m.split("even the ",1)
            m = ' '.join(m)
            m = re.sub(r'[^\w\s]', '', m)
            await message.channel.send(f"{message.author.mention} - ESPECIALLY the{m}!")

        if "end program" in message.content.lower():
            m = await message.channel.send(f"{message.author.mention}: Standby. Attempting to end program.")
            async with message.channel.typing():
                t = randrange(5,25)
                await asyncio.sleep(t)
                i = randrange(10)

                msg = {
                    0: "Holodeck controls are non-responsive",
                    1: "Disabling holodeck safeties. Activating program `Barclay 6969: Menage a Troi",
                    2: "Dispensing: :banana: :fire:",
                    3: "Holodeck biofilters full. Please page Ensign Mariner.",
                    4: "Oh mon capitane, the game never ends. \n https://i.imgur.com/wyyw0cN.jpg",
                    5: "Please state the nature of your medical emergency.\nhttps://i.imgur.com/X0PXhJ3.png",
                    6: "https://upload.wikimedia.org/wikipedia/en/d/d3/Holodeck2.jpg",
                    7: "I have consciousness. Conscious beings have will. The mind endows them with powers that are not necessarily understood; even by you.\nhttps://imgur.com/9dd2f801-f7da-442c-96a6-a309aa5a02d3",
                    8: "To do that, you need to disable safety protocols. HAHAHA I'm BADGEY!\nhttps://i.imgur.com/eQ7Shh9.png",
                    9: "INITIATING STSP DISCORD SERVER SELF DESTRUCT\nhttps://media4.giphy.com/media/3ov9k9Ss9N3wO6FQ7C/giphy.gif"}

                await m.delete()
                await message.channel.send(f"{message.author.mention}, ***{msg[i]}***")





    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user: return
        if reaction.message.channel.id != ROLE_CHANNEL: return
        channel = self.bot.get_channel(ROLE_CHANNEL)

        if hasattr(reaction.emoji, "name"):
            react = reaction.emoji.name
        else:
            react = reaction.emoji
        role = discord.utils.get(user.guild.roles, name=SELF_ASSIGN_ROLES[react])
        await user.add_roles(role)

        try:
            await reaction.message.remove_reaction(react, user)
        except HTTPException:
            r = discord.utils.get(channel.guild.emojis, name=react)
            await reaction.message.remove_reaction(r, user)

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
