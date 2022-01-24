# Standard library imports
import secrets
import traceback
from datetime import datetime
import time
import aiosqlite
# Library imports
import discord
import pytz
from discord.ext import commands

# Local imports
from utils.config import *
from utils.helpers import *

NO_REASON = "No reason given."
az_timezone = pytz.timezone('US/Arizona')


# ###---Class for ADMINISTRATIVE actions---####
class Moderators(commands.Cog, name="Moderator and Administrator Commands"):
    def __init__(self, client):
        self.bot = client

    # CHILL
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def chill(self, ctx, user: discord.Member, *reason: str):
        """ - Puts a user in 30 minute timeout"""
        role = discord.utils.get(ctx.guild.roles, name=TIMEOUT_ROLE_NAME)
        print(user)
        await user.add_roles(role)
        channel = self.bot.get_channel(MOD_ACTIONS_CHANNEL_ID)

        if not reason:
            reason = NO_REASON
        else:
            reason = ' '.join(reason)
        reason = remove_non_ascii(reason)
        # await ctx.message.delete()
        await channel.send(f"{user.mention} put in the brig by {ctx.message.author.mention} in "
                           f"{ctx.message.channel.mention}.\nReason: {reason}")
        await ctx.send(f"Hey {user.mention}, you need to chill out a bit. You've been given the `{role}` role."
                       f" This means you're stuck in "
                       f"{self.bot.get_channel(TIMEOUTCHAN).mention} for {TIMEOUT_MINUTES} minutes."
                       f" Be cool...\nReason: {reason}"
                       )

        # Add the action to the database
        async with aiosqlite.connect(DB_PATH) as db:
            # TIMESTAMP = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            sqlquery = """INSERT INTO naughtylist(discord_id, type, time, reason, by, active) VALUES (?,?,?,?,?, True)"""
            await db.execute(sqlquery, (user.id, NAUGHTY_TIMEOUT, timestamp, reason, ctx.message.author.id))
            await db.commit()

    # UNCHILL
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def unchill(self, ctx, user: discord.Member):
        """ - Removes timeout """
        role = discord.utils.get(ctx.guild.roles, name=TIMEOUT_ROLE_NAME)
        await user.remove_roles(role)
        channel = self.bot.get_channel(MOD_ACTIONS_CHANNEL_ID)
        await ctx.message.delete()

        async with aiosqlite.connect("db/db.sqlite") as db:
            await db.execute(f"UPDATE naughtylist SET active = 0 WHERE discord_id = {user.id}")
            await db.commit()

        time_out_channel = self.bot.get_channel(TIMEOUTCHAN)
        await channel.send(f"{user.mention}'s `{role}` role REMOVED by {ctx.message.author.mention}.")
        await time_out_channel.send(f"Hey {user.mention}, `{role}` role removed. welcome back! Be cool...")

    # BAN
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def ban(self, ctx, user: discord.Member, *why: str):
        """ - BAN a recruit """
        new_member = discord.utils.get(ctx.guild.roles, name=restricted)
        if not why:
            why = "No reason given"
        else:
            why = ' '.join(why)
            why = remove_non_ascii(why)
        if user.top_role == new_member or \
                discord.utils.get(ctx.message.author.roles, name=staff) is not None or \
                discord.utils.get(ctx.message.author.roles, name=mods) is not None:

            try:
                await user.ban(reason=why, delete_message_days=0)
            except Exception:
                await ctx.send(f'```py\n{traceback.format_exc()}\n```')
            else:
                channel = self.bot.get_channel(NOTES)
                await channel.send(f"<@{user.id}> `(<@{user.id}> {user.display_name})` BANNED "
                                   f"by {ctx.message.author.mention}. Reason: {why}")
                await ctx.message.delete()
                await ctx.send(f"<@{user.id}>  BANNED. Reason: {why}")

    # WELCOME
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def w(self, ctx, user: discord.Member = None):
        """ - Welcomes a user to the server and removes recruit role"""
        wchan = self.bot.get_channel(WELCOMECHAN)
        if ctx.channel == wchan:
            if not user:
                async for message in ctx.history(limit=2):
                    user = message.author
        if ctx.channel == wchan:
            role = discord.utils.get(ctx.guild.roles, name=restricted)
            await user.remove_roles(role)
            syslog = self.bot.get_channel(SYSLOG)

            await syslog.send(f"{user.mention} welcomed to the server by `{ctx.message.author.display_name}`")
            message = ("Thanks for introducing yourself. You now have full member access to our "
                       f"channels. Stop by <#{ROLE_CHANNEL}> and self-assign some permissions!")
            await ctx.send(f"{user.mention}, {message}")
            await ctx.message.delete()

    # NICKFIX
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def nickfix(self, ctx, user: discord.Member):
        """ - Uncancer a nickname (Removes non-ascii chars)"""
        channel = self.bot.get_channel(NOTES)
        if remove_non_ascii(user.display_name) == user.display_name and len(user.display_name.strip()) > 3:
            await ctx.send(f"No need to fix {user.mention}. It's not cancer.")
            return None
        try:
            nick = user.display_name
            try:
                newnick = remove_non_ascii(nick)
            except:
                newnick = f"cadet-{secrets.token_urlsafe(6)}"
            newnick = newnick.strip()
            if newnick == "" or len(newnick) <= 3:
                newnick = f"cadet-{secrets.token_urlsafe(6)}"
            await ctx.send(f"Hey {user.mention}. We don't like your nickname "
                           f"so we're changing it to `{newnick}`. Sorry / not sorry.")
            await user.edit(nick=newnick)
            await channel.send(f"NICKFIX: `{user.id}` -{user.mention} changed from "
                               f"`{nick}` to `{newnick}`")

        except:
            await ctx.send("Sorry, can't.")
            await channel.send(f'```py\n{traceback.format_exc()}\n```')

    # WARN
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def warn(self, ctx, user: discord.Member, *reason: str):
        """ - Sends a warning to a user"""
        if not reason:
            reason = NO_REASON
        else:
            reason = ' '.join(reason)
        reason = remove_non_ascii(reason)
        channel = self.bot.get_channel(MOD_ACTIONS_CHANNEL_ID)
        await ctx.message.delete()
        await ctx.send(f"{user.mention}, you've received a warning. Check your DMs for more details.")
        await channel.send(f"{user.mention}'s has been WARNED by {ctx.message.author.mention} in "
                           f"{ctx.message.channel.mention}.\nReason: {reason}")
        await user.send(f"Hey {user.mention}, you've been issued a warning for your actions "
                        f"in {user.guild.name}.\n Please understand that further actions will "
                        f"result in expulsion from the server.\n Reason: **{reason}**")

        # Add the action to the database
        async with aiosqlite.connect(DB_PATH) as db:
            TIMESTAMP = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            sqlquery = """INSERT INTO naughtylist(discord_id, type, time, reason, by, active) VALUES (?,?,?,?,?, 0)"""
            await db.execute(sqlquery, (user.id, NAUGHTY_WARN, TIMESTAMP, reason, ctx.message.author.id))


            await db.commit()

    # USER
    @commands.command(name='user_info', aliases=['user', 'info', 'userinfo', 'luser'])
    @commands.has_any_role(staff, mods)
    async def user_info(self, ctx, user: discord.Member):
        """ - Shows info about user, including warns & timeouts"""
        embed = discord.Embed()
        warns = ""
        warn_count = 0
        timeouts = ""
        timeout_count = 0

        async with aiosqlite.connect(DB_PATH) as db:
            results = await db.execute_fetchall(f"SELECT * FROM naughtylist WHERE discord_id = {int(user.id)}")
            print(results)
            for record in results:
                print(record)
                type = record[2]
                time = datetime.strptime(record[3], "%Y-%m-%d %H:%M:%S")
                time = time.astimezone(az_timezone)
                local_time = time.strftime("%m/%d %H:%M:%S")
                reason = record[4]
                active = record[6]
                submitted_by = await self.bot.fetch_user(int(record[5]))
                if active:
                    a = ":bangbang:"
                else:
                    a = ""
                if type == NAUGHTY_TIMEOUT:
                    timeouts += f"{local_time} by {submitted_by} `{reason}`{a}\n"
                    timeout_count += 1
                elif type == NAUGHTY_WARN:
                    warns += f"{local_time} by {submitted_by} `{reason}`\n"
                    warn_count += 1
                print(record[1])

        if warns == "":
            warns = "None"
        if timeouts == "":
            timeouts = "None"
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Name", value=user.mention, inline=True)
        embed.add_field(name="Discord ID", value=user.id, inline=True)
        embed.add_field(name=f"Warns: **{warn_count}**", value=warns, inline=False)
        embed.add_field(name=f"Time Outs: **{timeout_count}**", value=timeouts, inline=False)
        embed.set_footer(text="!! indicates active timeout")
        await ctx.send(content=f"ℹ information about **{user.name}**", embed=embed)

    # PURGE
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def purge(self, ctx, user: discord.Member, count: int):
        """ - Requires user and number of the user's messages. See: !help purge
            Purge <count> number of messages sent by <user>. Max <count> is 100
        messages from <user>. Looks for the <user>'s messages within the last 1000
        messages sent in the channel. Ex: !purge @ultraman 69"""

        # Purge algorithm is probably inefficient for deep purges, but easier to use for
        # moderators becuase it purges exactly the number of messages requested.

        MAX_PURGES = 100  # limit to how many messages will be purged.
        MAX_HISTORY = 1000  # how many messages into the history to look
        DISCORD_MSG_LIMIT = 2000
        if count > MAX_PURGES:
            count = MAX_PURGES
        log_channel = self.bot.get_channel(DELETEDMSGLOG)
        purge_log = ''
        history = ctx.channel.history(limit=MAX_HISTORY)

        try:
            for i in range(count):
                msg = await history.get(author=user)  # get the most recent message to purge
                if msg:
                    await msg.delete()
                    purge_log = f"`<{msg.author.name}> {msg.created_at.strftime('%Y-%m-%d %H:%M')}:`" + \
                                f"{msg.content}\n" + purge_log
                else:  # no more messages to purge
                    count = i
                    break
        except discord.errors.NotFound:
            pass
        except discord.errors.HTTPException:
            pass

        purge_log = f"Purged {count} messages by {user.mention}. Initiated by {ctx.message.author.mention} " \
                    f"in {ctx.message.channel.mention}:\n" + purge_log

        for short_purge_log in groups(purge_log, DISCORD_MSG_LIMIT):
            await log_channel.send(short_purge_log)  # 2000 character max

        try:
            await ctx.message.delete()  # delete the purge command message
        except discord.errors.NotFound:  # happens when a moderator purges themself
            pass

    # ROLELIST
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def rolelist(self, ctx, rolename="all"):
        """ - List all members with role name"""

        async with ctx.typing():
            userlist = f"| {'Name'.ljust(27)} | {'Joined at'.ljust(22)}|\n| " \
                       f"--------------------------- | --------------------- |\n"
            try:
                roleis = discord.utils.get(ctx.guild.roles, name=rolename)
            except:
                roleis = None
            if roleis is None:
                await ctx.send(f"No (or invalid) role specified, returning full user list.")
                for m in ctx.guild.members:
                    if m.joined_at is None:
                        joined = "Unavailable"
                    else:
                        joined = m.joined_at.strftime('%Y-%m-%d')
                    try:
                        userlist += (f"| {str(remove_non_ascii(str(m.display_name))).ljust(27)} "
                                     f"| {joined.ljust(22)}|\n")
                    except:
                        await ctx.send(f'```py\n{traceback.format_exc()}\n```')

            else:
                await ctx.send(f"Role: `{rolename}`  -  Member Count: `{len(roleis.members)}`")
                for m in roleis.members:
                    if m.joined_at is None:
                        joined = "Unavailable"
                    else:
                        joined = m.joined_at.strftime('%Y-%m-%d')
                    try:
                        userlist += (f"| {str(remove_non_ascii(str(m.display_name))).ljust(27)} "
                                     f"| {joined.ljust(22)}|\n")
                    except:
                        await ctx.send(f'```py\n{traceback.format_exc()}\n```')
            try:
                n = 15
                splitlist = [userlist.splitlines(True)[i * n:(i + 1) * n] for i in
                             range((len(userlist.splitlines(True)) + n - 1) // n)]
                for l in splitlist:
                    await ctx.send(f"```markdown\n{''.join(l)}```")
            except:
                await ctx.send(f'```py\n{traceback.format_exc()}\n```')

    # INTRO
    @commands.command()
    @commands.has_any_role(staff, mods)
    async def nudge(self, ctx):
        """ - Sends message to new users in welcome channel"""
        wc = self.bot.get_channel(WELCOMECHAN)
        if ctx.message.channel == wc:
            await ctx.message.delete()
            role = discord.utils.get(ctx.guild.roles, name=restricted)
            await ctx.send("As a protection against spam and bots, new members are restricted to only talking "
                           f"in <#{WELCOMECHAN}>. "
                           f" Please say hi or introduce yourself to request access."
                           f" {role.mention}")


def setup(client):
    client.add_cog(Moderators(client))
