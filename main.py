import discord, os, pymongo
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
os.system('pip install PyNaCl dnspython')
token = str(os.getenv('TOKEN'))
prefix = str(os.getenv('PREFIX'))
intents = discord.Intents.default()
intents.members = False
bot = commands.Bot(command_prefix=['?'], intents=intents)
red = 0xF04747
green = 0x43B581
orange = 0xFAA61A
css1 = ''
addedword = False
pswd = os.getenv('DB')
client = pymongo.MongoClient(f"mongodb+srv://bot:{pswd}@cluster0.qrff5.mongodb.net/db?retryWrites=true&w=majority")
db = client.database
guild = db['guild']
whitelist = db['whitelist']


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    await bot.change_presence(activity=discord.Game(name=f'{prefix}help'))
    bot.remove_command('help')
    extensions = ['utils.help', 'utils.mod', 'utils.music', 'utils.poll']
    if __name__ == '__main__':
        for extension in extensions:
            bot.load_extension(extension)

@bot.event
async def on_command_error(ctx, e):
    print(e)
    embed=discord.Embed(title="An error occoured:", description=f"```{e}```", color=red)
    embed.set_footer(text="If you can't understand the reason of this error contact my owner.")
    await ctx.send(embed=embed)

@bot.command()
async def load(ctx, extension):
  if ctx.author.id == 776713998682292274:
    bot.load_extension(extension)
    await ctx.send('Done')

@bot.command()
async def unload(ctx, extension):
  if ctx.author.id == 776713998682292274:
    bot.unload_extension(extension)
    await ctx.send('Done')

@bot.command()
async def reload(ctx, extension):
  if ctx.author.id == 776713998682292274:
    bot.unload_extension(extension)
    bot.load_extension(extension)
    await ctx.send('Done')

@bot.command()
async def info(ctx, member: discord.Member):
    embed = discord.Embed(color=green)
    embed.add_field(name=":information_source:", value=f"{member.mention} joined at {member.joined_at} and has {len(member.roles)} roles.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    link = await ctx.channel.create_invite(max_age=0)
    embed = discord.Embed(color=green)
    embed.add_field(name=":white_check_mark:", value=f"This is your invite link: {str(link)}", inline=True)
    await ctx.send(embed=embed)



@bot.event
async def on_message(m: discord.Message) -> None:
  ctx = await bot.get_context(m)
  await bot.process_commands(m)
  a = guild.find_one({"_id": str(m.guild.id)})
  if ctx.valid:
    pass
  else:
    if m.guild:
      if m.author.id != bot.user.id:
        if not m.author.bot:
            if a["filter"] is True:
                with open('badwords.txt', 'r') as f:
                    badwords = f.read()
                if whitelist.find({"_id": str(m.guild.id), "whitelist": {"$all": [str(m.author.id)]}}).count() > 0:
                    return
                if m.content.startswith('e'):
                    return
                if m.attachments:
                    return
                if m.is_system():
                    return
                with open('badwords.txt', 'r') as f:
                    words = f.read()
                    badwords = words.split()
                for words in badwords:

                    global addedword
                    global css1

                    list1 = m.content.lower().split(' ')

                    def check():
                        if guild.find({"_id": str(m.guild.id), "badWords": {"$all": [list1]}}).count() > 0:
                            return True
                        else:
                            return False
                    msg = m.content.lower().split(' ')

                    if words in msg or check() is True:
                        css1 = ""
                        if m.author.guild_permissions.administrator or m.author.guild_permissions.manage_guild or m.author.guild_permissions.manage_messages:
                            await m.delete()
                            await m.channel.send(
                                f"Heya, I can't ban you because you're an admin.... Just type '?whitelist {m.author.mention}' to disable me for you in this server. ")
                            pass
                        else:
                            await m.reply(f'You got a warn into the {m.guild.name} server {m.author.mention}!')
                            await m.delete()
                            if not guild.find({'_id': str(m.guild.id), str(m.author.id): 1}).count() > 0 and guild.find({'_id': str(m.guild.id), str(m.author.id): 2}).count() == 0 and guild.find({'_id': str(m.guild.id), str(m.author.id): 3}).count() == 0:
                                query = {"_id": str(m.guild.id)}
                                new = {"$set": {str(m.author.id): 1}}
                                try:
                                    query1 = {"_id": str(
                                        m.guild.id), str(m.author.id): 1}
                                    guild.insert_one(query1)
                                except:
                                    guild.update_one(query, new)

                            else:
                                if not guild.find({'_id': str(m.guild.id), str(m.author.id): 2}).count() > 0 and guild.find({'_id': str(m.guild.id), str(m.author.id): 1}).count() > 0:
                                    query = {"_id": str(m.guild.id)}
                                    new = {"$set": {str(m.author.id): 2}}
                                    guild.update_one(query, new)
                                else:
                                    if not guild.find({'_id': str(m.guild.id), str(m.author.id): 3}).count() > 0 and guild.find({'_id': str(m.guild.id), str(m.author.id): 2}).count() > 0:
                                        query = {"_id": str(m.guild.id)}
                                        new = {"$set": {str(m.author.id): 3}}
                                        guild.update_one(query, new)
                                    else:
                                        if not guild.find({'_id': str(m.guild.id), str(m.author.id): 2}).count() > 0 and guild.find({'_id': str(m.guild.id), str(m.author.id): 3}).count() > 0:
                                            query = {"_id": str(m.guild.id)}
                                            new = {
                                                "$unset": {str(m.author.id): 3}}
                                            guild.update_one(query, new)
                                            await m.author.ban(reason='Banned by the server bot. Reason: swearing.')
                                            user = bot.get_user(m.author.id)
                                            try:
                                                await user.send(f'You just got banned from {m.guild.name}.')
                                            except:
                                                pass





bot.run(str(token), bot=True)