import asyncio
from datetime import datetime

import aiosqlite
import nextcord as discord
from nextcord.ext import tasks, commands
from revChatGPT.V1 import Chatbot
from utils.config import *


class Tasks(commands.Cog, name="Automatic Tasks"):
    def __init__(self, client):
        self.bot = client
        self.check_timeouts.start()

    def cog_unload(self):
        self.check_timeouts.cancel()

    @tasks.loop(hours=5)
    async def pop_cgtp_conversations(self):
        CHATGPT_CONFIG = {"access_token": CGPT_TOKEN}
        chatbot = Chatbot(config=CHATGPT_CONFIG)

        for userid in CONVERSATIONS:
            if userid['last_updated'] < datetime.datetime.now()-datetime.timedelta(hours=1):
                "foo"
                chatbot.delete_conversation(userid['conversation'])



    @tasks.loop(minutes=5)
    async def check_timeouts(self):
        print("Checking timeouts")
        modlog_channel = self.bot.get_channel(SYSLOG)
        role = discord.utils.get(modlog_channel.guild.roles, name=TIMEOUT_ROLE_NAME)
        timeout_channel = self.bot.get_channel(TIMEOUTCHAN)

        async with aiosqlite.connect(DB_PATH) as db:
            sqlstring = "SELECT * FROM naughtylist WHERE active = 1"
            results = await db.execute_fetchall(sqlstring)
            print(results)

            for record in results:
                user = modlog_channel.guild.get_member(int(record[1]))
                time = datetime.strptime(record[3], "%Y-%m-%d %H:%M:%S")
                now = datetime.utcnow()
                minutes_diff = (now - time).total_seconds() / 60.0
                print(f"Now: {now}\nTime:{time}\nDiff; {minutes_diff}")

                if minutes_diff >= TIMEOUT_MINUTES:
                    await timeout_channel.send(f"{user.mention} - Your timeout has elapsed and you're welcome back "
                                               f"to the rest of the server. Please be cool.")
                    await user.remove_roles(role)
                    sqlstring = f"UPDATE naughtylist SET active = 0 WHERE discord_id = {int(record[1])}"
                    print(sqlstring)
                    await db.execute(sqlstring)
                    await modlog_channel.send(f"{user.mention}'s `{role}` role"
                                              f" REMOVED automatically after {TIMEOUT_MINUTES} minutes.")
            await db.commit()

    @check_timeouts.before_loop
    async def before_check_timeouts(self):
        print('waiting...')
        await self.bot.wait_until_ready()
        await asyncio.sleep(5)


def setup(client):
    client.add_cog(Tasks(client))
