import discord
from discord.ext import commands
import asyncio
from urllib.parse import quote
import urllib.request
import re

class Youtube(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["yt"])
    async def youtube(self,ctx,*,title):
        video_id = []
        sq = f'https://www.youtube.com/results?search_query={quote(title)}&sp=EgIQAQ%253D%253D'# quote приабразуем удобочитаемасть для адресной строки
        data = urllib.parse.urlencode({'Host': 'search.cpsa.ca', 'Connection': 'keep-alive', 'Content-Length': 23796,'Origin': 'http://search.cpsa.ca', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Cahce-Control': 'no-cache', 'X-Requested-With': 'XMLHttpRequest','X-MicrosoftAjax': 'Delta=true', 'Accept': '*/*','Referer': 'http://search.cpsa.ca/PhysicianSearch','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6','Cookie': 'ASP.NET_SessionId=kcwsgio3dchqjmyjtwue402c; _ga=GA1.2.412607756.1459536682; _gat=1'})
        data = data.encode('ascii')
        doc = urllib.request.urlopen(sq,data).read().decode('cp1251', errors='ignore')
        match = re.findall(r"\?v\=(.+?)\"", doc)# Ищем на стронички все эти символы
        if not(match is None):#Если мы нашли
            for ii in match:
                if (len(ii) < 25):#25 потомучто в строке поиска ютуба максимму 25 символов
                    video_id.append(ii)

        video_id = dict(zip(video_id, video_id)).values()#Очищаем од дублей

        video_id = list(video_id)
        await ctx.send(f'https://www.youtube.com/watch?v={video_id[0]}')

def setup(bot):
    bot.add_cog(Youtube(bot))
