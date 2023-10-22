from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@client.event
@bot.event
async def on_ready():
    print(f'Logged in as {client.user}.')
    print(f'Logged in as {bot.user}.')

@client.event
@bot.event
async def on_message(message):
    if message.author == client.user:
    if message.author == bot.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")
    await bot.process_commands(message)

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')
@bot.command(description='Say hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(description='Callback')
async def call(ctx):
    await ctx.send('Callback!')

try:
    client.run(TOKEN)
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
    print("Improper token has been passed.")
