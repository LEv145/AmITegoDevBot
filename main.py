import discord
import os
import config
import random
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix=config.PREFIX)
bot.remove_command('help') 


for filename in os.listdir('./Modules'):
    if filename.endswith('.py'):
        bot.load_extension(f'Modules.{filename[:-3]}')

bot.run(config.TOKEN)
