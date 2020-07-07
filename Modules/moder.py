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

        await ctx.send(f"Удалено {amount} сообщений")

    @commands.command(pass_context = True,aliases=['поиск','g','google','читай'],description="Это сообщение",usage="search [интернет запрос]")
    async def search( ctx,*, amount: str):
        if not amount:
            await ctx.send("Пожалуйста, используйте такую кострукцию: `!!search [интернет запрос]`")
        a = '+'.join(amount.split())
        embed=discord.Embed(title=f"{amount}", url=f'https://google.gik-team.com/?q={a}', color=0xff7a0d)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moder(client))
