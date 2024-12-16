# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 799_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 441 bytes
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!", intents=(discord.Intents.default()))

@bot.slash_command()
async def shutdown(ctx):
    await ctx.respond("Shutting down...")
    await bot.close()


bot.run("YOUR_TOKEN_HERE")

# okay decompiling 799_1.pyc
