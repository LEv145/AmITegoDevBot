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
                description=f"{ctx.author.display_name}, Чтоб узнать список команд пропишите !!хелп <модуль>\n"
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
                    description=f"{ctx.author.display_name}, Модуль не найден!\nЧтоб узнать список команд пропишите !!хелп <модуль>\n"
                                f"**Доступные модули:** {''.join(cogs)}")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(information(client))
