# Импорт
import discord
import config
from Utils import DB
from discord.ext import commands


# Код
class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.cog_name = ["Ивенты", True]

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if str(message.channel.id) in DB.Get().options("channels")[1]:
                like = self.bot.get_emoji(671667959617552386)
                dislike = self.bot.get_emoji(671667959386603520)
                await message.add_reaction(like)
                await message.add_reaction(dislike)
        except Exception as a:
            print("ERROR")
            print(a)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        async def create(category, channel):
            if int(after.channel.id) == int(channel):
                cat = discord.utils.get(member.guild.categories, id=int(category))
                channel2 = await member.guild.create_voice_channel(
                    name=f"{member.name}#{member.discriminator}",
                    category=cat)
                await member.move_to(channel2)
                await channel2.set_permissions(member, manage_channels=True)
                Set.privateChannels(channel2, member)

        Get = DB.Get()
        Set = DB.Set()

        if after.channel:
            channel = Get.options("channels")[0]
            category = Get.options("category")[0]

            if Get.privateChannels(member):
                if Get.privateChannels(member)[0] == '0':
                    await create(category, channel)
                else:
                    if before.channel:
                        if str(before.channel.id) in str(Get.privateChannels(member)[0]):
                            try:
                                await before.channel.delete()
                                Set.privateChannels('0', member)

                                await create(category, channel)
                            except Exception as a:
                                print("Ошибка в Приватках")
                                print(a)

                    else:
                        await create(category, channel)
            else:
                await create(category, channel)
        else:
            if before.channel:
                if Get.privateChannels(member) and Get.privateChannels(member) != '0':
                    if str(before.channel.id) in str(Get.privateChannels(member)[0]):
                        try:
                            await before.channel.delete()
                            Set.privateChannels('0', member)
                        except Exception as a:
                            print("Ошибка в Приватках")
                            print(a)


def setup(client):
    client.add_cog(events(client))
