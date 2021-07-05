import discord
from datetime import datetime
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(861630100524499015)
        embed = discord.Embed(title="New Member!", description=f"{member.mention}, Welcome to this awesome server!!!", colour=discord.Colour.dark_red(), timestamp=datetime.utcnow())
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(861630100524499015)
        embed = discord.Embed(title="Lost Member :(", description=f"{member.mention} has left the server :(", colour=discord.Colour.dark_red(), timestamp=datetime.utcnow())
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))