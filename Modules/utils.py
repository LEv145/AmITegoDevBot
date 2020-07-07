# Импорт
import discord  # Discord
import config
import json
import requests
import re
import urllib.request
from urllib.parse import quote
from discord.ext import commands  # Discord


# Класс
class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Ультилиты"]

    @commands.command(
        aliases=['коронавирус', "covid", 'ковид'],
        description="Информация о коронавирусе.",
        usage="коронавирус <Страна>")
    async def covide(self, ctx, country=None):
        if not country:
            await ctx.send(f"Введите название страны на английском языке с заглавной буквы")
        else:
            for item in json.loads(requests.get("https://corona.lmao.ninja/v2/countries").text):
                if item['country'] == country:
                    embed = discord.Embed(
                        title=f'Статистика Коронавируса | {country}',
                        color=config.COLOR_GOOD)
                    embed.add_field(name=f'Выздоровело:', value=f'{item["recovered"]} человек')
                    embed.add_field(name=f'Заболеваний:', value=f'{item["cases"]} человек')
                    embed.add_field(name=f'Погибло:', value=f'{item["deaths"]} человек')
                    embed.add_field(name=f'Заболеваний за сутки:', value=f'+{item["todayCases"]} человек')
                    embed.add_field(name=f'Погибло за сутки:', value=f'+{item["todayDeaths"]} человек')
                    embed.add_field(name=f'Проведено тестов:', value=f'{item["tests"]} человек')
                    embed.add_field(name=f'Активные зараженные:', value=f'{item["active"]} человек')
                    embed.add_field(name=f'В тяжелом состоянии:', value=f'{item["critical"]}  человек')
                    embed.set_thumbnail(url=item["countryInfo"]['flag'])
                    embed.set_footer(text=config.COPYRIGHT_TEXT, icon_url=config.COPYRIGHT_ICON)

                    return await ctx.send(embed=embed)

    @commands.command(
        aliases=["yt"],
        description="Поиск на Ютуб.",
        usage="yt <Название>")
    async def youtube(self, ctx, *, title):
        video_id = []
        sq = f'https://www.youtube.com/results?search_query={quote(title)}&sp=EgIQAQ%253D%253D'  # quote приабразуем удобочитаемасть для адресной строки
        data = urllib.parse.urlencode({'Host': 'search.cpsa.ca', 'Connection': 'keep-alive', 'Content-Length': 23796,
                                       'Origin': 'http://search.cpsa.ca',
                                       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                       'Cahce-Control': 'no-cache', 'X-Requested-With': 'XMLHttpRequest',
                                       'X-MicrosoftAjax': 'Delta=true', 'Accept': '*/*',
                                       'Referer': 'http://search.cpsa.ca/PhysicianSearch',
                                       'Accept-Encoding': 'gzip, deflate',
                                       'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
                                       'Cookie': 'ASP.NET_SessionId=kcwsgio3dchqjmyjtwue402c; _ga=GA1.2.412607756.1459536682; _gat=1'})
        data = data.encode('ascii')
        doc = urllib.request.urlopen(sq, data).read().decode('cp1251', errors='ignore')
        match = re.findall(r"\?v\=(.+?)\"", doc)  # Ищем на стронички все эти символы
        if not (match is None):  # Если мы нашли
            for ii in match:
                if (len(ii) < 25):  # 25 потомучто в строке поиска ютуба максимму 25 символов
                    video_id.append(ii)

        video_id = dict(zip(video_id, video_id)).values()  # Очищаем од дублей

        video_id = list(video_id)
        await ctx.send(f'https://www.youtube.com/watch?v={video_id[0]}')


def setup(client):
    client.add_cog(utils(client))
