from discord.ext import commands
import os, asyncio, discord
from dotenv import load_dotenv
load_dotenv()
red = 0xF04747
green = 0x43B581
orange = 0xFAA61A

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        pre = os.getenv('PREFIX')
        page = {}
        page['1'] = discord.Embed(title='Help page 1/3', color=green)
        page['1'].add_field(name=f"{pre}addword",
                            value=f"Add a custom swear word to your server! Simple type '{pre}addword XXXX' where XXXX is your own custom word to add. At the moment you can add 1 custom word per server.",
                            inline=False)
        page['1'].add_field(name=f"{pre}rmword",
                            value=f"Remove a custom swear word from your server's custom badwords! Simple type '{pre}rmword XXXX' where XXXX is your own custom word to remove. You can only remove custom words.",
                            inline=False)
        page['1'].add_field(name=f"{pre}kick",
                            value=f"Kick a member, use \"{pre}kick @user_mention <optional reason>\".",
                            inline=False)
        page['1'].add_field(name=f"{pre}infractions",
                            value=f"Check how many infractions an user has! Simply use '{pre}infractions @user_ping' where @user_ping is a ping to the user to check.",
                            inline=False)
        page['1'].add_field(name=f"{pre}clearall",
                            value=f"Clear all the infractions for an user. Simply type '{pre}clearall @user_ping' where @user_ping is a ping to the user you want to clear all warns.",
                            inline=False)

        page['2'] = discord.Embed(title='Help page 2/3', color=green)
        
        page['2'].add_field(name=f"{pre}ban",
                            value=f"Ban a member, use \"{pre}ban @user_mention <optional reason>\".",
                            inline=False)
        page['2'].add_field(name=f"{pre}unban",
                            value=f"Unban a member, use \"{pre}unban USERID\".",
                            inline=False)
        page['2'].add_field(name=f"{pre}mute",
                            value=f"Mute an user. To use this command create a \"Muted\" role without the \"Send messages\" permission. Then type \"{pre}mute @user_mention\" where @user_mention is a mention to the user to mute.",
                            inline=False)
        page['2'].add_field(name=f"{pre}unmute",
                            value=f"Unmute an user. To use this command you have to mute the user first and type \"{pre}unmute @user_mention\" where @user_mention is a mention to the user to unmute.",
                            inline=False)
        page['2'].add_field(name=f"{pre}invite",
                            value="Create an instant invite to your server. Note that the generated invite will never expire and it has unlimited uses.",
                            inline=False)


        page['3'] = discord.Embed(title='Help page 3/3', color=green)
        
        page['3'].add_field(name=f"{pre}info",
                            value=f"Get info of a member, use \"{pre}info @user_mention\".",
                            inline=False)
        page['3'].add_field(name=f"{pre}purge",
                            value=f"Purge as many messages as you want, use \"{pre}purge 1234\" where the 1234 is the number of messages you want to delete.",
                            inline=False)
        page['3'].add_field(name=f"{pre}cleanup",
                            value=f"Purge the last 40 messages up.",
                            inline=False)
        page['3'].add_field(name=f"{pre}play",
                            value=f"Play a song. Just join a voice channel and type \"{pre}play <song query>\". Song query can be either a youtube url or a text to search.",
                            inline=False)
        page['3'].add_field(name=f"{pre}stop",
                            value=f"Stop the current playing song.",
                            inline=False)
        page['3'].add_field(name="Contribute", value="To contribute to this bot just open a pull request on GitHub.")
        number = 1
        pagination = await ctx.send(embed=page[str(number)])
        await pagination.add_reaction('⏪')
        await pagination.add_reaction('⬅️')
        await pagination.add_reaction('⏹')
        await pagination.add_reaction('➡️')
        await pagination.add_reaction('⏩')

        def check(reaction, user):
            return reaction.emoji in ['⬅️', '➡️', '⏹', '⏩', '⏪'] and user == ctx.author

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=600, check=check)
            except asyncio.TimeoutError:
                await pagination.delete()
                break
            else:
                if reaction.emoji == '➡️':
                    number += 1
                    try:
                        await reaction.remove(ctx.author)
                    except:
                        pass
                    try:
                        await pagination.edit(embed=page[str(number)])
                    except KeyError:
                        number = 1
                        await pagination.edit(embed=page[str(number)])
                elif reaction.emoji == '⬅️':
                    number -= 1
                    try:
                        await reaction.remove(ctx.author)
                    except:
                        pass
                    try:
                        await pagination.edit(embed=page[str(number)])
                    except KeyError:
                        number = 3
                        await pagination.edit(embed=page[str(number)])
                elif reaction.emoji == '⏹':
                    try:
                        await pagination.clear_reactions()
                    except:
                        pass
                    break
                elif reaction.emoji == '⏩':
                    number = 3
                    try:
                        await reaction.remove(ctx.author)
                    except:
                        pass
                    try:
                        await pagination.edit(embed=page[str(number)])
                    except KeyError:
                        number = 3
                        await pagination.edit(embed=page[str(number)])
                elif reaction.emoji == '⏪':
                    number = 1
                    try:
                        await reaction.remove(ctx.author)
                    except:
                        pass
                    try:
                        await pagination.edit(embed=page[str(number)])
                    except KeyError:
                        number = 3
                        await pagination.edit(embed=page[str(number)])


def setup(bot):
    bot.add_cog(Help(bot))
