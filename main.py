import discord
import os
import random
import asyncio
from discord.ext import commands, tasks
import json
from config import PREFIX, TOKEN




bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command('help')


#Загружаю коги
@bot.command()
async def load(ctx, extensions):
    bot.load_extensions(f'cogs.{extensions}')#Загрузка дополнений
    await ctx.send('loaded')

#Разгрузка
@bot.command()
async def reload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')#Розгрузка дополнений
    await ctx.send('unloaded')

@bot.command()
async def unload(ctx, extensions):
    bot.unload_extension(f'cogs.{extensions}')#Розгрузка дополнений
    bot.load_extensions(f'cogs.{extensions}')#Загрузка дополнений
    await bot.send('unload')





for filename in os.listdir('./cgs'): # Цикл перебирающий файлы в cogs
    if filename.endswith('.py'): # если файл кончается на .py, то это наш ког
        bot.load_extension(f'cgs.{filename[:-3]}')# загрузка дополнений







bot.run(TOKEN)
