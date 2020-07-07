import discord
import asyncio
from discord.ext import commands
import aiohttp
import wikipedia # pip install wikipedia
from bs4 import BeautifulSoup
import requests 
from discord.utils import get


class BotWikipedia(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
        self._last_member = None
        self.cog_name = ["Википедия"]


	@commands.command(
		aliases=["today"],
		description="Показывает события сегодняшнего дня в мировой истории.",
		usage="сегодня")
	async def сегодня(self, ctx):
		wikipedia.set_lang('ru')
		text = wikipedia.summary('Шаблон:События дня')
		e = discord.Embed(description = text, colour = discord.Color.light_grey())
		e.set_author( name = f'История дня', icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711186981832360046/240_F_314623540_fFZYeWk6U9LEDrQQ27gN0gEPCTWAaai5.png')
		e.set_footer( text = 'Wikipedia', icon_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
		await ctx.send(embed = e) 

	@commands.command(
		aliases=["статья", "википедия", "wiki", "wikipedia"],
		description="Показывает самую популярную статью в википедии по запросу.",
		usage="вики [запрос]"
	)
	async def вики(self, ctx, *, reason):
		try:
			wikipedia.set_lang('ru')
			text = wikipedia.summary(f'{reason}', sentences=5)
			e = discord.Embed(description = text, colour = discord.Color.light_grey() )
			e.add_field( name = 'Запрос:', value = f'{reason}')
			e.set_author( name = f'Поиск по запросу', icon_url = 'https://image.flaticon.com/icons/png/512/148/148928.png')
			e.set_footer( text = 'Wikipedia', icon_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
			await ctx.send( embed = e)
		except:
			e = discord.Embed()
			e.set_author( name = f'Википедия:', icon_url = 'https://image.flaticon.com/icons/png/512/148/148928.png')
			e.add_field(name="Ошибка:", value="Не получилось ничего найти по Вашему запросу",inline=False)
			e.add_field(name="Решение:",value="Уточните запрос, добавив ключевые слова и/или попробуйте другой запрос")
			e.set_footer(text="Извиняемся, за предоставленные неудобства.")
			await ctx.send(embed = e)
	@commands.command(
		aliases=["news","новости", "важное"],
		description="показывает нынешние важные события во всём мире.",
		usage="события"
	)
	async def события(self, ctx):
		wikipedia.set_lang('ru')
		text = wikipedia.summary('Шаблон:Текущие_события_на_заглавной_странице')
		e = discord.Embed(description = text, colour = discord.Color.light_grey() )
		e.set_author( name = f'Новости', icon_url = 'https://media.discordapp.net/attachments/689879530542071952/713692320393854996/calendar.png?width=407&height=407')
		e.set_footer( text = 'Wikipedia', icon_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
		await ctx.send( embed = e)

	@commands.command(
		aliases = ["избранная_статья"],
		description="показывает текущую избранную статью в википедии.",
		usage="избранное"
	)
	async def избранное(self, ctx):
		wikipedia.set_lang('ru')
		text = wikipedia.summary('Шаблон:Текущая избранная статья')
		e = discord.Embed(description = text, colour = discord.Color.light_grey() )
		e.set_author( name = f'Избранная статья', icon_url = 'https://media.discordapp.net/attachments/640123959135698954/711188654806007818/seo-and-web.png?width=407&height=407')
		e.set_footer( text = 'Wikipedia', icon_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
		await ctx.send( embed = e) 

	@commands.command(
		aliases = ["факты_вики", "факты_википедия", "викифакты"],
		description="показывает интересные факты из википедии.",
		usage="факты"
	)
	async def факты(self, ctx):
		wikipedia.set_lang('ru')
		text = wikipedia.summary('Шаблон:Знаете_ли_вы')
		e = discord.Embed(description = text, colour = discord.Color.light_grey() )
		e.set_author( name = f'Интересные факты', icon_url = 'https://media.discordapp.net/attachments/689879530542071952/711186172700917770/circle.png?width=407&height=407')
		e.set_footer( text = 'Wikipedia', icon_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
		await ctx.send( embed = e) 

	@commands.command(
		aliases=["изображение_дня", "image", "day_image"]
		description="показывает изображение дня",
		usage="изображение дня"
	)
	async def изображение(self, ctx):
		wikiimage = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
		#делаем запрос на самом сайте
		full_page = requests.get(wikiimage, headers=headers)
		#Делаю так чтоб мы парсели через библиотеку бютифулл суп
		soup = BeautifulSoup(full_page.content, 'html.parser')
		#Нахожу все нужные елементы 
		convert = soup.find('a', {'class':'image'})
		clr = (random.randint(0,16777215))
		e = discord.Embed(color = clr)
		e.set_author(name="Изображение дня", icon_url="https://cdn3.iconfinder.com/data/icons/spring-2-1/30/Camera-128.png")
		e.set_image(url=f"https:{convert.img['src']}")
		e.set_footer(text=f"{convert.img['alt']}")
		await ctx.send(embed = e)


def setup(bot):
    client.add_cog(BotWikipedia(bot))
    print("Готова википедия!")
