import time
import config
import discord
from Utils import DB
from colorama import Style, Fore
from discord.ext import tasks, commands


class Loop(commands.Cog):
    def __init__(self, bot):
        self.mute_loop.start()
        self.cog_name = ["Лупы", True]
        self.bot = bot

    @tasks.loop(seconds=5.0)
    async def mute_loop(self):
        try:
            for mem in DB.Get().mute(None):
                mute = mem[1]
                guild = self.bot.get_guild(658658120309932062)
                if guild:
                    member = guild.get_member(int(mem[0]))
                    if member:
                        if float(mute) <= float(time.time()):
                            DB.Set().mute(member, 0)
                            mute_role = discord.utils.get(guild.roles, name="Muted")
                            await member.remove_roles(mute_role, reason="Снят Мьют Временем", atomic=True)

        except Exception as e:
            print(Fore.RED + "[ERROR] " + Style.RESET_ALL + f"В цикле MUTE_LOOP произошла следующая ошибка:")
            print(Fore.RED + "[ERROR] " + Style.RESET_ALL + f"{e}")
            print(Fore.RED + "[ERROR] " + Style.RESET_ALL + f"Цикл MUTE_LOOP продолжает свою работу!")


def setup(client):
    client.add_cog(Loop(client))
