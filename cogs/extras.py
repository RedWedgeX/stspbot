import nextcord as discord
from nextcord.ext import commands
from utils.config import *
import traceback
import google.generativeai as genai
import os
import time
import json
import aiosqlite

class Extras(commands.Cog, name="Stuff for funzies"):
    def __init__(self, client):
        self.bot = client
        self.user_chats = {}  # Initialize user_chats here


    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def enable(self, ctx):
        async with ctx.typing():
            self.bot.cgpt_enabled = True
            await ctx.send("BadgeyGPT Enabled")

    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def disable(self, ctx):
        async with ctx.typing():
            self.bot.cgpt_enabled = False
            await ctx.send("BadgeyGPT Disabled")

    @commands.command(hidden=True)
    @commands.has_any_role(staff)
    async def script(self, ctx, movie):
        try:
            chanid =  918285694122721351
            chan = self.bot.get_channel(int(chanid))
            await ctx.send(f"connecting to {chan.name}")
            vc = await chan.connect()

            vc.play(discord.FFmpegPCMAudio(f'scripts/{movie}.mp3'))
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send


    @commands.command(hidden=True)
    async def gg(self, ctx):
        history = await load_chat_history_for_user(ctx.author.id)
        print(history)

    @commands.command(hidden=True)
    async def gemni(self, ctx, *prompt: str):
        async with ctx.message.channel.typing():

            user_id = ctx.author.id
            prompt = ' '.join(prompt)
            system_instructions = GEMINI_PROMPT

            history = await load_chat_history_for_user(user_id)

            genai.configure(api_key=os.getenv("GEMINI_API"))
            model = genai.GenerativeModel(
                model_name="gemini-1.5-pro",
                system_instruction=system_instructions +  f" \n\n Info about the user you're chatting with:\n"
                                                          f" Their user name is {ctx.message.author.name}.\n"
                                                          f"You can @ mention them as {ctx.message.author.mention}.\n "
                                                          f"Their nickname in this server is {ctx.message.author.nick}.",
            )
            chat = model.start_chat(history=history)

            print(ctx.author.name)

            await add_chat_history(user_id, "user", prompt)

            try:
                response = chat.send_message(prompt)
                await add_chat_history(user_id, "model", response.text)
                # chat.history.append({"role": "model", "parts": response.text})

                # Split response into chunks of 2000 characters or less
                response_text = response.text
                for i in range(0, len(response_text), 2000):
                    await ctx.send(response_text[i:i+2000])
            except Exception as e:
                await ctx.send(f'```py\n{traceback.format_exc()}\n```')

async def add_chat_history(user_id, role, parts):
    async with aiosqlite.connect(DB_PATH) as db:
        timestamp = time.time()
        await db.execute("INSERT INTO chat_history (user_id, role, parts, timestamp) "
                         "VALUES (?, ?, ?, ?)", (user_id, role, parts, timestamp))
        await db.commit()

async def load_chat_history_for_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        rows = await db.execute_fetchall(f"SELECT role, parts FROM chat_history WHERE user_id = {int(user_id)} ORDER BY timestamp")
        results_as_dicts = [{"role": entry[0], "parts": entry[1]} for entry in rows]
        return results_as_dicts


def setup(client):
    client.add_cog(Extras(client))
