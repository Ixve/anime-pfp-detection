import sys
import os
import os.path
import discord
import asyncio
import subprocess
from discord.ext import commands
from discord import Member

bot = commands.Bot(",", self_bot=True)
token = "Put your token here"

@bot.event
async def on_ready():
    print("Bot ready!")

@bot.command()
async def avatar(ctx, member: discord.User = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send("Attempting to detect gay: {}".format(userAvatar))
    os.system("curl {} --output $XDG_DATA_HOME/animeface-ruby/temp.webp".format(userAvatar))
    with open('f.txt', 'w') as f:
        subprocess.call(['ruby', '$XDG_DATA_HOME/animeface-ruby/sample.rb', './temp.webp'], stdout=f)            
    with open('f.txt', 'r') as c:
        c1 = c.read()
        sw = "\nSee temp_out.png\n"
        if sw in c1:
            os.system("bash $XDG_DATA_HOME/animeface-ruby/t.sh")
            with open('$XDG_DATA_HOME/animeface-ruby/data.json', 'r') as v:
                v1 = v.read()
                await ctx.send(v1)
        else:
            await ctx.send("No face detected")
            


bot.run(token, bot=False)
