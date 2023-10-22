import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command(description='Say hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(description='Callback')
async def call(ctx):
    await ctx.send('Callback!')

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
