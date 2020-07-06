import discord
import os,random,asyncio
from discord.ext import commands, tasks
import json




bot = commands.Bot(command_prefix='!!')
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



with open('token.txt','r') as f:
    token = f.read()



bot.run(token)
