import sys
import os
import os.path
import discord
import asyncio
import subprocess
from discord.ext import commands
from discord import Member

bot = commands.Bot(",", self_bot=True)
token = "YOUR TOKEN HERE"

@bot.event
async def on_ready():
    print("Bot ready!")

@bot.command()
async def avatar(ctx, member: discord.User = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send("Attempting to detect gay: {}".format(userAvatar))
    os.system("curl {} --output ./temp.png".format(userAvatar))        
    os.system("python3 ./detect.py")
    os.system("bash ./upload.sh")
    with open("./data1.json", "r") as f:
        x = f.readlines()
        await ctx.send("Returned data: {}".format(x))

bot.run(token, bot=False)
