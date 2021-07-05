import discord
from discord.ext import commands


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="ping")
    async def ping_command(self, ctx):
        embed = discord.Embed(title="Pong!", description=f"The bot's latency is {round(self.bot.latency * 1000)}ms")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meta(bot))