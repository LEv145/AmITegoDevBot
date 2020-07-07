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
        aliases=["рандом", "rand", "ранд", "рандомное_число", "rand_num"],
        description="Это сообщение",
        usage="rand [первое число] [второе число]")
    async def random(self, ctx, num1: float = 1, num2: float = 100):
        await ctx.send(f'Ваше число: {random.randint(num1,num2)}')
      

def setup(client):
    client.add_cog(Fun(client))
