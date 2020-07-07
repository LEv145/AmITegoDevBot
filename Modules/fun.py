# Импорт
import discord
import config
import random
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
        aliases=["сапер", "sap", "saper"],
        description="Сыграть в сапер",
        usage="сапер")
    async def sap(self, ctx):
        await ctx.message.delete() 

        r_list = ['🟩','🟧','🟥']

        msg = await ctx.send(f'Выберете сложность :\n\n{r_list[0]}— Easy\n{r_list[1]}— Medium\n{r_list[2]}— Hard')
        for r in r_list:
            await msg.add_reaction(r)
        try:
            react, user = await self.Bot.wait_for('reaction_add', timeout= 30.0, check= lambda react, user: user == ctx.author and react.message.channel == ctx.channel and react.emoji in r_list)
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
                await ctx.send('Неверная реакция!', delete_after= 10.0)
            
        bombs = columns * rows - 1
        bombs = bombs / 2.5
        bombs = round(random.randint(5, round(bombs)))

        columns = int(columns)
        rows = int(rows)
        bombs = int(bombs)
        
        grid = [[0 for num in range (columns)] for num in range(rows)]

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

            for (adj_y, adj_x) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:

                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:

                        adj_sum = adj_sum + 1
                except Exception as error:
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
            description= final,
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

        await msg.edit(embed= emb, content= None)
def setup(client):
    client.add_cog(Fun(client))
