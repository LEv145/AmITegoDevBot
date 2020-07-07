# Импорт
import discord
import config
from discord.ext import commands


# Код
class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Информация"]

    @commands.command(
        aliases=["хелп", "команды", "comms", "commands", "помощь"],
        description="Это сообщение",
        usage="хелп [модуль]")
    async def help(self, ctx, name=None):
        prefix = config.PREFIX
        color = config.COLOR_GOOD

        copy_text = config.COPYRIGHT_TEXT
        copy_icon = config.COPYRIGHT_ICON

        cogs = []
        for i in self.bot.cogs:
            cog = self.bot.cogs[i]
            hide = len(cog.cog_name)
            if hide == 1:
                cogs.append(f"{cog.cog_name[0]}")

        if not name:
            embed = discord.Embed(
                description=f"{ctx.author.display_name}, Чтоб узнать список команд пропишите {config.PREFIX}хелп <модуль>\n"
                            f"**Доступные модули:** {', '.join(cogs)}")
            await ctx.send(embed=embed)
        else:
            if name in cogs:
                cog = None
                namec = None
                for i in self.bot.cogs:
                    coge = self.bot.cogs[i]
                    if name in coge.cog_name:
                        cog = coge
                        namec = i
                        break

                name = cog.cog_name[0]
                comm_list = []

                for command in self.bot.commands:
                    if command.cog_name == namec:
                        if not command.hidden:
                            comm_list.append(
                                f"**{command.aliases[0]}:** {command.description}\n`{prefix}{command.usage}`\n\n")

                embed = discord.Embed(
                    title=f"Хелп | {name}",
                    description=f"".join(comm_list),
                    color=color)
                embed.set_footer(text=copy_text, icon_url=copy_icon)
                embed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/695787093242282055/707320024473534485/what.png')

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    description=f"{ctx.author.display_name}, Модуль не найден!\nЧтоб узнать список команд пропишите {config.PREFIX}хелп <модуль>\n"
                                f"**Доступные модули:** {', '.join(cogs)}")
                await ctx.send(embed=embed)

    @commands.command(
        aliases=['сервер', 'серверинфо'],
        description="Информация о сервере")
    async def server(self, ctx):

        members = ctx.guild.members
        bots = len([m for m in members if m.bot])
        users = len(members) - bots
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)

        embed = discord.Embed(title=f"{ctx.guild.name}", color=config.COLOR_GOOD, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name=f"Пользователей", value=f"<:user:703271496411250709> Участников: **{users}**\n"
                                                     f"<:bot:703271496457650329> Ботов: **{bots}**\n"
                                                     f"<:online1:703271496616902716> Онлайн: **{online}**\n"
                                                     f"<:online2:703271496595800304> Отошёл: **{idle}**\n"
                                                     f"<:online3:703271496260255785> Не Беспокоить: **{dnd}**\n"
                                                     f"<:noonline2:703271496658714634> Оффлайн: **{offline}**")

        embed.add_field(name=f"Каналов", value=f"<:voice:703271496474296441> Голосовые: **{allvoice}**\n"
                                               f"<:text:703271496566440136> Текстовые: **{alltext}**\n")

        embed.add_field(name=f"Количество Ролей", value=f"{allroles}")
        embed.add_field(name=f"Создатель сервера", value=f"{ctx.guild.owner}")
        embed.add_field(name=f"Регион сервера", value=f"{ctx.guild.region}")
        embed.add_field(name=f"Дата создания сервера", value=f"{ctx.guild.created_at.strftime('%b %#d %Y')}")

        embed.set_footer(text=config.COPYRIGHT_TEXT, icon_url=config.COPYRIGHT_ICON)
        await ctx.send(embed=embed)

    # О боте
    @commands.command(
        aliases=['бот', 'bot', 'инфо', "информация"],
        description="Информация о боте.")
    async def bote(self, ctx):
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count

        embedinfo = discord.Embed(title=f"Информация О Боте",
                                  description="**Кто такой FsokyCommBot**\nЭто бот который создан специально для Fsoky Community.\nОн является OpenSource ботом вклад в которого может сделать любой пользователь который знаком с GitHub",
                                  color=config.COLOR_GOOD)
        embedinfo.set_thumbnail(url=self.bot.user.avatar_url)
        embedinfo.add_field(name=f"Серверов:", value=len(self.bot.guilds), inline=True)
        embedinfo.add_field(name=f"Пользователей:", value=members, inline=True)
        embedinfo.add_field(name="‎‎‎‎", value="‎", inline=True)
        embedinfo.add_field(name=f"Создатель Бота:", value=f"don#4170", inline=True)
        embedinfo.add_field(name=f"Бот Использует:", value=f"Python, SQLite3", inline=True)
        embedinfo.add_field(name=f"Пинг Бота:", value=f"{self.bot.ws.latency * 1000:.0f} ms", inline=True)
        embedinfo.add_field(name=f"GitHub Бота:", value=f"https://github.com/DSvinka-Codes/FsokyCommBot", inline=True)
        embedinfo.set_footer(text=config.COPYRIGHT_TEXT, icon_url=config.COPYRIGHT_ICON)
        await ctx.send(embed=embedinfo)


def setup(client):
    client.add_cog(information(client))
