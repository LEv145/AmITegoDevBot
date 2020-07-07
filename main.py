import os
import config
import discord
from Modules.loops import Loop
from discord.ext import commands
from colorama import Fore, Style  # Цветная консоль
from colorama import init  # Цветная консоль


TOKEN = config.TOKEN
PREFIX = config.PREFIX
STATUS = config.STATUS
COLOR_ERROR = config.COLOR_ERROR

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')
init()


# Запуск Бота
@client.event
async def on_ready():
    print(" ")
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(
        Fore.CYAN + '|' + Style.RESET_ALL + f' Смена статуса на стандартный... ' + Fore.CYAN + '|' + Style.RESET_ALL)
    await client.change_presence(activity=discord.Game(name=STATUS))
    print(
        Fore.CYAN + '|' + Style.RESET_ALL + f'        Бот активирован!         ' + Fore.CYAN + '|' + Style.RESET_ALL)
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(f'  Статус   - {STATUS}          ')
    print(f'  Имя бота - {client.user.name}')
    print(f'  ID бота  - {client.user.id}  ')
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(" ")

    loop = Loop(client)
    try:
        loop.activator()
    except AssertionError:
        pass


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Команда не найдена!', color=COLOR_ERROR))
    elif isinstance(error, commands.MissingPermissions):
        return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, У бота недостаточно прав!\n'
                                                              f'❗️ Если это не модераторская команда: то значит у бота нету права управлением сообщениями или права на установку реакций.', color=color))
    elif isinstance(error, commands.MissingPermissions) or isinstance(error, discord.Forbidden):
        return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, У вас недостаточно прав!', color=COLOR_ERROR))
    elif isinstance(error, commands.BadArgument):
        if "Member" in str(error):
            return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Пользователь не найден!', color=COLOR_ERROR))
        if "Guild" in str(error):
            return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Сервер не найден!', color=COLOR_ERROR))
        else:
            return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Введён неверный аргумент!', color=COLOR_ERROR))
    elif isinstance(error, commands.MissingRequiredArgument):
        return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Пропущен аргумент с названием {error.param.name}!', color=COLOR_ERROR))
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Воу, Воу, Не надо так быстро прописывать команды.\n'
                                                       f'❗️ Подожди {error.retry_after:.2f} секунд и сможешь написать команду ещё раз.'))
    else:
        if "ValueError: invalid literal for int()" in str(error):
            return await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, Укажите число а не строку!', color=COLOR_ERROR))
        else:
            print(Fore.RED + f"[ERROR] " + Style.RESET_ALL + f"Команда: {ctx.message.content}")
            print(Fore.RED + f"[ERROR] " + Style.RESET_ALL + f"Сервер:  {ctx.message.guild}")
            print(Fore.RED + f"[ERROR] " + Style.RESET_ALL + f"Ошибка:  {error}")
            await ctx.send(embed=discord.Embed(description=f'❗️ {ctx.author.name}, \n**`ERROR:`** {error}', color=COLOR_ERROR))
            raise error


for filename in os.listdir('./Modules'):
    if filename.endswith('.py'):
        client.load_extension(f'Modules.{filename[:-3]}')

client.run(TOKEN)
