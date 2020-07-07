# Импорт
import discord  # Discord
import config
import json
import requests
from discord.ext import commands  # Discord


# Класс
class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Ултилиты"]

    @commands.command(
        aliases=['коронавирус', "covid", 'ковид'],
        description="Информация о коронавирусе.")
    async def covide(self, ctx, country=None):
        if not country:
            await ctx.send(f"Введите название страны на английском языке с заглавной буквы")
        else:
            for item in json.loads(requests.get("https://corona.lmao.ninja/v2/countries").text):
                if item['country'] == country:
                    embed = discord.Embed(
                        title=f'Статистика Коронавируса | {country}',
                        color=config.color)
                    embed.add_field(name=f'Выздоровело:', value=f'{item["recovered"]} человек')
                    embed.add_field(name=f'Заболеваний:', value=f'{item["cases"]} человек')
                    embed.add_field(name=f'Погибло:', value=f'{item["deaths"]} человек')
                    embed.add_field(name=f'Заболеваний за сутки:', value=f'+{item["todayCases"]} человек')
                    embed.add_field(name=f'Погибло за сутки:', value=f'+{item["todayDeaths"]} человек')
                    embed.add_field(name=f'Проведено тестов:', value=f'{item["tests"]} человек')
                    embed.add_field(name=f'Активные зараженные:', value=f'{item["active"]} человек')
                    embed.add_field(name=f'В тяжелом состоянии:', value=f'{item["critical"]}  человек')
                    embed.set_thumbnail(url=item["countryInfo"]['flag'])
                    embed.set_footer(text=config.copy, icon_url=config.icon)

                    return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(utils(client))
