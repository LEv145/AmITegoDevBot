# Импорт
import discord
import config
from discord.ext import commands


# Код
class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Модераторские"]

    @commands.command(
        aliases=["клеар", "clr", "cls", "очистить", "очст"],
        description="Это сообщение",
        usage="clear [количество сообщений для удаления]")
    @commands.has_permissions( manage_messages = True)
    async def clear( ctx, amount: int ):
        if not amount:
              await ctx.send("Пожалуйста, используйте такую кострукцию: `!!clear [количество сообщений для удаления]`")
              return
        await ctx.channel.purge( limit =  (amount + 1) )

        await ctx.sent(f"Удалено {amount} сообщений")
      

def setup(client):
    client.add_cog(Moder(client))
