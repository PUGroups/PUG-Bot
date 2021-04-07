from discord.ext import commands
import os, asyncio, discord
from dotenv import load_dotenv
load_dotenv()
red = 0xF04747
green = 0x43B581
orange = 0xFAA61A

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, question):
        embed = discord.Embed(color=green, title=f":bar_chart: {question}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🔼')
        await msg.add_reaction('🔽')






def setup(bot):
    bot.add_cog(Poll(bot))
