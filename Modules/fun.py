# Импорт
import discord
import asyncio
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
      

def setup(client):
    client.add_cog(Fun(client))
