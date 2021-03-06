import discord
from discord.ext import commands
import random

dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']


class RandomThings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll_dice')
    async def roll_dice(self, ctx, count):
        res = [random.choice(dashes) for _ in range(int(count))]
        await ctx.send(" ".join(res))

    @commands.command(name='randint')
    async def my_randint(self, ctx, min_int, max_int):
        num = random.randint(int(min_int), int(max_int))
        await ctx.send(num)


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send("Спасибо за сообщение")
        if "привет" in message.content.lower():
            await message.channel.send("И тебе привет")

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )


TOKEN = "ODM2MzAxMTU3MTQ0MDY4MTI2.YIcAJQ.LsVkpOJXS26qo4AQrj2amEm6oQ4"
bot = commands.Bot(command_prefix='!#')
bot.add_cog(RandomThings(bot))
bot.run(TOKEN)