# Импорт
import discord
import config
import random
import sqlite3,datetime
from discord.ext import commands


# Код
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Фановые"]
    db = sqlite3.connect("Marry.db")#подклучаем бд
	cursor = db.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS marrys(
	id1 BIGINT,
    id2 BIGINT,
    datem TEXT
    )""")
	db.commit()
	db.close()
    @commands.command(
        aliases=["рандом", "рандомайзер", "random"],
        description="Рандомайзер",
        usage="рандом [первое число] [второй число]")
    async def randomizer(self, ctx, number1=1, number2=100):
        await ctx.message.delete()
        try:
            if not number1:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:",value="Вы забыли написать цельные числа!")
                embed.add_field(name="Решение:",value="Введите команду с 2 цельными числами (`/рандомайзер 1 10`)",inline=False)
                await ctx.send(embed=embed)
                return
            elif not number2:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:",value="Отсутствует 2 число!")
                embed.add_field(name="Решение:",value="Введите 2 цельное число!",inline=False)
                await ctx.send(embed=embed)
                return
            elif int(number1) > 1_000_000 or int(number2) > 1_000_000:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:",value="Превышение лимита!")
                embed.add_field(name="Решение:",value="Введите цельное число от 0 до 1млн!",inline=False)
                await ctx.send(embed=embed)
                return
            else:
                number1 = int(number1)
                number2 = int(number2)
                if number1 != number2:
                    e = discord.Embed()
                    e.set_author(name="Утилиты: рандомайзер",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                    e.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                    e.add_field(name="Число:",value=f" {random.randint(number1, number2)}")
                    e.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                    message_with_random = await ctx.send(embed=e)
                    popitka = 0
                    while popitka < 4:
                        em = discord.Embed()
                        em.set_author(name="Утилиты: рандомайзер",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                        em.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                        em.add_field(name="Число:",value=f" {random.randint(number1, number2)}")
                        em.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                        await message_with_random.edit(embed=em)
                        popitka += 1
                        await asyncio.sleep(0.3)
                    if popitka == 4:
                        em = discord.Embed()
                        em.set_author(name="Утилиты: рандомайзер",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                        em.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                        em.add_field(name="Число:",value=f"__** {random.randint(number1, number2)}**__")
                        em.add_field(name = "‎‎‎‎",value=f"{random.randint(number1, number2)}")
                        await message_with_random.edit(embed=em)
                elif number1 == number2:
                    e = discord.Embed()
                    e.set_author(name="Ошибка!",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                    e.add_field(name="Проблема:",value="Указанные аргументы одинаковы!")
                    e.add_field(name="Решение:",value="Введите 2 разных цельных числа, чтобы бот смог создать диапазон из чисел",inline=False)
                    await ctx.send(embed=e)
        except ValueError:
            e = discord.Embed()
            e.set_author(name="Ошибка!",icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
            e.add_field(name="Проблема:",value="Введено не цельное число!")
            e.add_field(name="Решение:",value="Введите цельное число!",inline=False)
            await ctx.send(embed=e)
            
    @commands.command(
        aliases=["поженится", "marry"],
        description="Поженится с юзером",
        usage="поженится [Пользователь] чтобы принять написать в чат "Да" Чтобы отклнить написать в чат "Нет" ")
	async def marry(self, ctx, user:discord.User= None):
		db = sqlite3.connect("Marry.db") 
		cursor = db.cursor()
		no_one = []
		if user != None:
			if user == ctx.message.author:
				await ctx.send('Вы не можете жениться на себе')
			else:
				cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
				res = cursor.fetchall() 
				cursor.execute(f"SELECT * FROM marrys WHERE id1='{user.id}' OR id2='{user.id}'")
				res1 = cursor.fetchall()
				if not res:
					await ctx.send(f'{user.mention}, хотите ли вы поженеться с {ctx.message.author.mention}? (Напишите : Да или Нет)')
					try:
						msg = await self.client.wait_for('message', timeout=300.0, check=lambda message: message.author == user)
					except asyncio.TimeoutError:
						await ctx.send('Увы, но время ожидание вышло.')
						db.close()
					else:
						if msg.content.lower() == 'да':
							cursor.execute(f"INSERT INTO marrys(id1, id2, datem) VALUES({ctx.message.author.id}, {user.id}, '{datetime.date.today()}')")
							db.commit()
							await ctx.send(f'Поздровляю! Теперь {ctx.message.author.mention} и {user.mention} женаты!')   
							db.close()
						elif msg.content.lower() == 'нет':
							await ctx.send(f'{ctx.message.author.mention}, мне жаль, но вам отказали.')
							db.close()
				else:
					if not res == no_one:
						await ctx.send('Вы уже женаты')
					elif not res1 == no_one:
						await ctx.send('Этот пользователь уже женат.')
				db.close()            
		elif user == None:
			cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
			res = cursor.fetchall()
			if not res:
				await ctx.send('Вы не женаты.')
				db.close()
			else:
				res = res[0]
				if res[0] == ctx.message.author.id:
					await ctx.send(f"Вы женаты с {self.Bot.get_user(res[1])}, вы женились {res[2].replace('-', '.')}")  
					db.close()
				elif res[1] == ctx.message.author.id:
					await ctx.send(f"Вы женаты с {self.Bot.get_user(res[0])}, вы женились {res[2].replace('-', '.')}")
					db.close()


	@commands.command(
        aliases=["развестись", "divorce" ],
        description="Развестить с пользователем",
        usage="развестись [Пользователь] чтобы принять написать в чат "Да" Чтобы отклнить написать в чат "Нет" ")
	async def divorce(self, ctx):
		db = sqlite3.connect("Marry.db")
		cursor = db.cursor()
		cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
		res = cursor.fetchall()
		if not res:
			await ctx.send('Вы не женаты.')
			db.close()
		else:
			await ctx.send(f'Вы точно хотите развестись?(Напишите : Да или Нет)')
			try:
				msg = await self.client.wait_for('message', timeout=10.0, check=lambda message: message.author == ctx.author)
			except asyncio.TimeoutError:
				await ctx.send('Увы, но время ожидание вышло.')
				db.close()
			else:
				if msg.content.lower() == 'да':
					cursor.execute(f"DELETE FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
					db.commit()
					db.close()
					await ctx.send('Вы развелись.')
				elif msg.content.lower() == 'нет':
					await ctx.send('Вы отменили команду.')
					db.close()         
            
       
      

def setup(client):
    client.add_cog(Fun(client))
