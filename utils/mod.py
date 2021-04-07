from discord.ext import commands
import os, asyncio, discord, pymongo
from dotenv import load_dotenv
from dotenv import load_dotenv
load_dotenv()
red = 0xF04747
green = 0x43B581
orange = 0xFAA61A
load_dotenv('/.env')
pswd = os.getenv('DB')
client = pymongo.MongoClient(f"mongodb+srv://bot:{pswd}@cluster0.qrff5.mongodb.net/db?retryWrites=true&w=majority")
db = client.database
guild = db['guild']
whitelist = db['whitelist']

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, aliases=['purge'])
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, limit1: int):
        limit = limit1 + 1
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(color=green)
        embed.add_field(name=":white_check_mark:", value=f"Purged {limit1} messages.", inline=True)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def cleanup(self, ctx):
        limit = 40
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(color=green)
        embed.add_field(name=":white_check_mark:", value=f"Cleared last 40 messages.", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Muted'))
        embed = discord.Embed(title=":white_check_mark:", description="**{0}** was muted by **{1}**.".format(member, ctx.message.author), color=orange)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        await member.remove_roles(discord.utils.get(member.guild.roles, name='Muted'))
        embed = discord.Embed(title=":white_check_mark:", description="**{0}** was unmuted by **{1}**.".format(member, ctx.message.author), color=green)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(color=orange)
        embed.add_field(name=":lock:", value=f"{member.mention} was banned by {ctx.author.mention}!", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: int):
        banned_users = await ctx.guild.bans()

        for ban_entry in banned_users:
            user = ban_entry.user
            if user.id == member:
                await ctx.guild.unban(user)
        embed = discord.Embed(color=green)
        embed.add_field(name=":unlock:", value=f"<@{member}> was unbanned by {ctx.author.mention}.", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
            await member.kick(reason=reason)
            embed = discord.Embed(color=orange)
            embed.add_field(name=":lock:", value=f"{member.mention} was kicked by {ctx.author.mention}.", inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addword(self, ctx, *, word):
        if ctx.guild:
            query = {"_id": str(ctx.guild.id)}
            new = {"$push": {"badWords": str(word)}}
            guild.update_one(query, new)

            embed = discord.Embed(color=green)
            embed.add_field(name=":white_check_mark:", value=f"Ok, I've added \"{word}\" to the server's blacklist.", inline=True)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rmword(self, ctx, *, word):
        if ctx.guild:
            query = {"_id": str(ctx.guild.id)}
            new = {"$pull": {"badWords": str(word)}}
            guild.update_one(query, new)

            embed = discord.Embed(color=green)
            embed.add_field(name=":white_check_mark:", value=f"Ok, I've removed \"{word}\" from the server's blacklist.", inline=True)
            await ctx.send(embed=embed)

        
    @commands.command(aliases = ['warns'])
    async def infractions(self, ctx, member: discord.Member):
        if ctx.guild:
            try:
                a = guild.find_one({"_id": str(ctx.guild.id)})
                b = a[str(member.id)]
                embed = discord.Embed(color=orange)
                embed.add_field(name=":white_check_mark:", value=f"{member.mention} has {b} warns.",
                                inline=True)
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(color=green)
                embed.add_field(name=":white_check_mark:", value=f"{member.mention} has no warns!",
                                inline=True)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearall(self, ctx, member: discord.Member):
        if ctx.guild:
            try:
                query = {"_id": str(ctx.guild.id)}
                new = {"$unset": {str(member.id) : 1}}
                guild.update_one(query, new)
                embed = discord.Embed(color=green)
                embed.add_field(name=":white_check_mark:",
                                value=f"All warns for {member.mention} where cleared!",
                                inline=True)
                await ctx.send(embed=embed)
            except:
                try:
                    query = {"_id": str(ctx.guild.id)}
                    new = {"$unset": {str(member.id) : 2}}
                    guild.update_one(query, new)
                    embed = discord.Embed(color=green)
                    embed.add_field(name=":white_check_mark:",
                                    value=f"All warns for {member.mention} where cleared!",
                                    inline=True)
                    await ctx.send(embed=embed)
                except:
                    try:
                        query = {"_id": str(ctx.guild.id)}
                        new = {"$unset": {str(member.id) : 3}}
                        guild.update_one(query, new)
                        embed = discord.Embed(color=green)
                        embed.add_field(name=":white_check_mark:",
                                        value=f"All warns for {member.mention} where cleared!",
                                        inline=True)
                        await ctx.send(embed=embed)
                    except:
                        embed = discord.Embed(color=green)
                        embed.add_field(name=":x:",
                                        value=f"{member.mention} has no wanrs!",
                                        inline=True)
                        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Moderation(bot))
