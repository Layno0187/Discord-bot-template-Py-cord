import discord
from discord.commands import slash_command
from discord.ext import commands

class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot:

def setup(bot):
    bot.add_cog(BAse(bot))
