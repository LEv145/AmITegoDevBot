# Импорт
import discord
import asyncio
import random
import sqlite3
import datetime
import requests
import json
from discord.ext import commands


# Код
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Фановые"]

    @commands.command(
        aliases=["рандом", "рандомайзер", "random"],
        description="Рандомайзер",
        usage="рандом [первое число] [второй число]")
    async def randomizer(self, ctx, number1=1, number2=100):
        await ctx.message.delete()
        try:
            if not number1:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",
                                 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:", value="Вы забыли написать цельные числа!")
                embed.add_field(name="Решение:", value="Введите команду с 2 цельными числами (`/рандомайзер 1 10`)",
                                inline=False)
                await ctx.send(embed=embed)
                return
            elif not number2:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",
                                 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:", value="Отсутствует 2 число!")
                embed.add_field(name="Решение:", value="Введите 2 цельное число!", inline=False)
                await ctx.send(embed=embed)
                return
            elif int(number1) > 1_000_000 or int(number2) > 1_000_000:
                embed = discord.Embed()
                embed.set_author(name="Ошибка!",
                                 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                embed.add_field(name="Проблема:", value="Превышение лимита!")
                embed.add_field(name="Решение:", value="Введите цельное число от 0 до 1млн!", inline=False)
                await ctx.send(embed=embed)
                return
            else:
                number1 = int(number1)
                number2 = int(number2)
                if number1 != number2:
                    e = discord.Embed()
                    e.set_author(name="Утилиты: рандомайзер",
                                 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                    e.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                    e.add_field(name="Число:", value=f" {random.randint(number1, number2)}")
                    e.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                    message_with_random = await ctx.send(embed=e)
                    popitka = 0
                    while popitka < 4:
                        em = discord.Embed()
                        em.set_author(name="Утилиты: рандомайзер",
                                      icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                        em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                        em.add_field(name="Число:", value=f" {random.randint(number1, number2)}")
                        em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                        await message_with_random.edit(embed=em)
                        popitka += 1
                        await asyncio.sleep(0.3)
                    if popitka == 4:
                        em = discord.Embed()
                        em.set_author(name="Утилиты: рандомайзер",
                                      icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                        em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                        em.add_field(name="Число:", value=f"__** {random.randint(number1, number2)}**__")
                        em.add_field(name="‎‎‎‎", value=f"{random.randint(number1, number2)}")
                        await message_with_random.edit(embed=em)
                elif number1 == number2:
                    e = discord.Embed()
                    e.set_author(name="Ошибка!",
                                 icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
                    e.add_field(name="Проблема:", value="Указанные аргументы одинаковы!")
                    e.add_field(name="Решение:",
                                value="Введите 2 разных цельных числа, чтобы бот смог создать диапазон из чисел",
                                inline=False)
                    await ctx.send(embed=e)
        except ValueError:
            e = discord.Embed()
            e.set_author(name="Ошибка!",
                         icon_url="https://media.discordapp.net/attachments/689879530542071952/728180075656118302/die-512.png?width=432&height=432")
            e.add_field(name="Проблема:", value="Введено не цельное число!")
            e.add_field(name="Решение:", value="Введите цельное число!", inline=False)
            await ctx.send(embed=e)

    @commands.command(
        aliases=["сапер", "saper"],
        description="Сыграть в сапер",
        usage="сапер <None>")
    async def sap(self, ctx):
        await ctx.message.delete()

        r_list = ['🟩', '🟧', '🟥']

        rows = None
        columns = None

        msg = await ctx.send(f'Выберете сложность :\n\n{r_list[0]}— Easy\n{r_list[1]}— Medium\n{r_list[2]}— Hard')
        for r in r_list:
            await msg.add_reaction(r)
        try:
            react, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda react,
                                                                                             user: user == ctx.author and react.message.channel == ctx.channel and react.emoji in r_list)
        except Exception:
            await msg.delete()
        else:
            if str(react.emoji) == r_list[0]:
                columns = 4
                rows = 4
                await msg.clear_reactions()
            elif str(react.emoji) == r_list[1]:
                columns = 8
                rows = 8
                await msg.clear_reactions()
            elif str(react.emoji) == r_list[2]:
                columns = 12
                rows = 12
                await msg.clear_reactions()
            else:
                await msg.delete()
                await ctx.send('Неверная реакция!', delete_after=10.0)

        bombs = columns * rows - 1
        bombs = bombs / 2.5
        bombs = round(random.randint(5, round(bombs)))

        columns = int(columns)
        rows = int(rows)
        bombs = int(bombs)

        grid = [[0 for num in range(columns)] for num in range(rows)]

        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)

            if grid[y][x] == 0:
                grid[y][x] = 'B'
                loop_count = loop_count + 1

            if grid[y][x] == 'B':
                pass

        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:

            adj_sum = 0

            for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                        adj_sum = adj_sum + 1
                except Exception:
                    pass

            if grid[pos_y][pos_x] != 'B':
                grid[pos_y][pos_x] = adj_sum

            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1

        not_final = []

        for the_rows in grid:
            not_final.append(''.join(map(str, the_rows)))

        not_final = '\n'.join(not_final)

        not_final = not_final.replace('0', '||:zero:||')
        not_final = not_final.replace('1', '||:one:||')
        not_final = not_final.replace('2', '||:two:||')
        not_final = not_final.replace('3', '||:three:||')
        not_final = not_final.replace('4', '||:four:||')
        not_final = not_final.replace('5', '||:five:||')
        not_final = not_final.replace('6', '||:six:||')
        not_final = not_final.replace('7', '||:seven:||')
        not_final = not_final.replace('8', '||:eight:||')
        final = not_final.replace('B', '||:bomb:||')

        percentage = columns * rows
        percentage = bombs / percentage
        percentage = 100 * percentage
        percentage = round(percentage, 2)

        emb = discord.Embed(
            description=final,
            color=0xC0C0C0
        )
        emb.add_field(
            name='Кол-во столбцов :',
            value=columns,
            inline=True
        )
        emb.add_field(
            name='Кол-во строк:',
            value=rows,
            inline=True
        )
        emb.add_field(
            name='Всего клеток :',
            value=columns * rows,
            inline=True
        )
        emb.add_field(
            name='Кол-во бомб:',
            value=bombs,
            inline=True
        )
        await msg.edit(embed=emb, content=None)

    @commands.command(
        aliases=["поженится"],
        description="Поженится с юзером",
        usage="поженится <Пользователь>")
    async def marry(self, ctx, user: discord.User = None):
        db = sqlite3.connect("Data/DataBase/Marry.db")
        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS marrys(
                            id1 BIGINT,
                            id2 BIGINT,
                            datem TEXT
                            )""")
        db.commit()

        no_one = []
        if user:
            if user == ctx.message.author:
                await ctx.send('Вы не можете жениться на себе')
            else:
                cursor.execute(
                    f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
                res = cursor.fetchall()
                cursor.execute(f"SELECT * FROM marrys WHERE id1='{user.id}' OR id2='{user.id}'")
                res1 = cursor.fetchall()
                if not res:
                    await ctx.send(
                        f'{user.mention}, хотите ли вы пожениться с {ctx.message.author.mention}? (Напишите : Да или Нет)')
                    try:
                        msg = await self.bot.wait_for('message', timeout=300.0,
                                                      check=lambda message: message.author == user)
                    except asyncio.TimeoutError:
                        await ctx.send('Увы, но время вышло.')
                        db.close()
                    else:
                        if msg.content.lower() == 'да':
                            cursor.execute(
                                f"INSERT INTO marrys(id1, id2, datem) VALUES({ctx.message.author.id}, {user.id}, '{datetime.date.today()}')")
                            db.commit()
                            await ctx.send(f'Поздравляю! Теперь {ctx.message.author.mention} и {user.mention} женаты!')
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
        elif not user:
            cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
            res = cursor.fetchall()
            if not res:
                await ctx.send('Вы не женаты.')
                db.close()
            else:
                res = res[0]
                if res[0] == ctx.message.author.id:
                    await ctx.send(f"Вы женаты с {self.bot.get_user(res[1])}, вы женились {res[2].replace('-', '.')}")
                    db.close()
                elif res[1] == ctx.message.author.id:
                    await ctx.send(f"Вы женаты с {self.bot.get_user(res[0])}, вы женились {res[2].replace('-', '.')}")
                    db.close()

    @commands.command(
        aliases=["развестись"],
        description="Развестить с пользователем",
        usage="развестись <Пользователь>")
    async def divorce(self, ctx):
        db = sqlite3.connect("Data/DataBase/Marry.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
        res = cursor.fetchall()
        if not res:
            await ctx.send('Вы не женаты.')
            db.close()
        else:
            await ctx.send(f'Вы точно хотите развестись? (Напишите : Да или Нет)')
            try:
                msg = await self.bot.wait_for('message', timeout=70.0,
                                              check=lambda message: message.author == ctx.author)
            except asyncio.TimeoutError:
                await ctx.send('Увы, но время вышло.')
                db.close()
            else:
                if msg.content.lower() == 'да':
                    cursor.execute(
                        f"DELETE FROM marrys WHERE id1='{ctx.message.author.id}' OR id2='{ctx.message.author.id}'")
                    db.commit()
                    db.close()
                    await ctx.send('Вы развелись.')
                elif msg.content.lower() == 'нет':
                    await ctx.send('Вы отменили команду.')
                    db.close()

    @commands.command(aliases=['поиск', 'g', 'google', 'читай'], description="Бот загуглить вместо тебя",
                      usage="search <интернет запрос> | [Юзер]")
    async def search(self, ctx, *, amount: str):
        member=None
        if not amount:
            await ctx.send(
                "Пожалуйста, используйте такую кострукцию: `!!search [запрос] | [Юзер]`")

        await ctx.channel.purge(limit=1)
        
        list_ = amount.split('|')
        
        if len(list_) >= 2:
            member = list_[-1]
            del list_[-1]
                     
        amount = '|'.join(list_)
        a = '+'.join(amount.split())

        if member:
            await ctx.send(member)
        embed = discord.Embed(title=f"{amount}", url=f'https://google.gik-team.com/?q={a}', color=0xff7a0d)

        await ctx.send(embed=embed)

    @commands.command(aliases=['доки', 'документация'], description="Документация", usage="доки <None>")
    async def doc(self, ctx):
        content = """
        Основа: https://bit.ly/2Z7FOC7
        Минимальная инструкция по установке: https://bit.ly/3gvnF74
        Быстрый старт: https://bit.ly/2CjesQn
        API: https://bit.ly/3iHqJPB
        FAQ: https://bit.ly/326Q1kn       
        """
        embed = discord.Embed(title="Профессиональная документация!", description=content, color=0xff7a0d)
        await ctx.send(embed=embed)

    @commands.command(aliases=["кот"], description="Выведет рандомного кота", usage="кот <None>")
    async def cat(self, ctx):
        for item in json.loads(requests.get("https://api.thecatapi.com/v1/images/search").text):
            embed = discord.Embed(color=discord.Color.blue())
            embed.set_image(url=item["url"])
            await ctx.send(embed=embed)
            break

    @commands.command(aliases=["собака"], description="Выведет рандомную собаку", usage="собака <None>")
    async def dog(self, ctx):
        response = requests.get('https://api.thedogapi.com/v1/images/search')
        json_data = json.loads(response.text)
        url = json_data[0]['url']

        embed = discord.Embed(title="Вот собачка! Гаф!", color=0xff9900)
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["панда"], description="Выведет рандомную панду", usage="панда <None>")
    async def panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/panda')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["птица"],
        description="Выведет рандомную птицу",
        usage="птица <None>")
    async def bird(self, ctx):
        response = requests.get('https://some-random-api.ml/img/birb')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["лиса"],
        description="Выведет рандомную лиск",
        usage="лиса <None>")
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["коала"],
        description="Выведет рандомную коалу",
        usage="коала <None>")
    async def koala(self, ctx):
        response = requests.get('https://some-random-api.ml/img/koala')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["красная_панда"],
        description="Выведет рандомную красную панду",
        usage="красная_панда <None>"
    )
    async def red_panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/red_panda')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['лотерея', 'рандомный_человек', 'rand_membed'], description="Лотерея на всём сервере",
                      usage="лотерея <None>")
    async def lottery(self, ctx):
        member = random.choice(ctx.guild.members)
        await ctx.send(f"{member.display_name} - счастливчик")
                                   
    @commands.command(aliases=["монетка" 'орел_решка','о_р','орёл_решка'],description='Бот подбрасывает монетку',usage='монетка <None>')
    async def o_r(self, ctx):
        robot = ("орёл", "решка")
        robot_choice = random.choice(robot)
        if robot_choice == "орёл":
            emb = discord.Embed(title="Орел или решка", colour=discord.Colour.red(), timestamp=ctx.message.created_at)
            emb.add_field(name="Подбрасываем монетку....", value="**Орёл**")
            emb.set_author(name="⠀", icon_url="https://www.iconpacks.net/icons/2/free-dollar-coin-icon-2139-thumb.png")
            emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)

        if robot_choice == "решка":
            emb = discord.Embed(title="Орел или решка", colour=discord.Colour.red(), timestamp=ctx.message.created_at)
            emb.add_field(name="Подбрасываем монетку....", value="**Решка**")
            emb.set_author(name="⠀", icon_url="https://www.iconpacks.net/icons/2/free-dollar-coin-icon-2139-thumb.png")
            emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
                                   

    @commands.command(aliases=["кнб", "камень_ножницы_бумага"],description='Игра в камень-ножницы-бумага',usage='кнб <камень/ножницы/бумага>')
    async def rsp(self,ctx, mess):
        robot = ['Камень', 'Ножницы', 'Бумага']
        stone_list = ["stone", "камень","к"]
        paper_list = ["paper", "бумага", "б"]
        scissors_list = ["scissors", "ножницы","н"]  
                                   
        out = {"icon": None, "value": None, "img": None}
                                   
        robot_choice = random.choice(robot)  
                                   
        win_list = ["Вы выиграли!","Вы проиграли :с", "Ничья!"]
            
        # Embed
        emb = discord.Embed(title=robot_choice, colour=discord.Colour.red(), timestamp=ctx.message.created_at)
                                   
        if mess.lower() in stone_list:       
            if robot_choice == 'Ножницы':
                win = win_list[0]
                out["icon"] = "✂"
            elif robot_choice == 'Бумага':
                win = win_list[1]
                out["icon"] = "🧻"
            else:
                win = win_list[2]
                out["icon"] = "🥔"

        elif mess == "Бумага" or mess == "Б" or mess == "бумага" or mess == "б":
            if robot_choice == 'Камень':
                win = win_list[0]
                out["icon"] = "🥔"     
            elif robot_choice == 'Ножницы':
                win = win_list[1]
                out["icon"] = "✂"             
            else:
                win = win_list[2]
                out["icon"] = "🧻"               

        elif mess == "Ножницы" or mess == "Н" or mess == "ножницы" or mess == "н":
            if robot_choice == 'Бумага':
                win = win_list[0]
                out["icon"] = "🧻"               
            elif robot_choice == 'Камень':
                win = win_list[1]
                out["icon"] = "🥔"                
            else:
                win = win_list[2]  
                out["icon"] = "✂"                 
                
        if win == "Вы выиграли!":
            out["img"] = "https://im0-tub-ru.yandex.net/i?id=12af96d2422023b2e8c0854c6960d229&n=13&exp=1"
        elif win == "Вы проиграли :с":
            out["img"] = "https://thumbs.dreamstime.com/b/%D0%BF%D0%BE%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-87995106.jpg"
        else:
            out["img"] = "https://avatanplus.com/files/resources/original/574454ca56620154e2eb3672.png"
                                   
        emb.add_field(name=out["icon"], value=win)
        emb.set_author(name="⠀",
        icon_url=out["img"])
        emb.set_footer(icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Fun(client))
