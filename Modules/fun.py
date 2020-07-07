# Импорт
import discord
import config
from discord.ext import commands


# Код
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Фан"]

    @commands.command(
        aliases=["рандом", "rand", "ранд", "рандомное_число", "rand_num"],
        description="Это сообщение",
        usage="хелп [модуль]")
    async def rand(ctx, num1: float = 1, num2: float = 100):
      if not num1 or not num2:
        await ctx.send("Пожалуйста, используйте такую кострукцию: `!!rand [первое число (начало)] [Второе число (конец)]`")

      await ctx.send(f'Ваше число: {random.randint(num1,num2)}')
      



def setup(client):
    client.add_cog(Fun(client))
