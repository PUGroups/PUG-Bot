import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('hello to you too!')
  if message.content.startswith('what the fuck'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('wtf'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('bitch'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('fuck off'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('he\'s black'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('she\'s black'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('whore'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('hoe'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')
  if message.content.startswith('asshole'):
    await message.channel.send(':rotating_light: use of inappropriate word :rotating_light:, Please review our Code of Conduct here:- https://www.pugroups.in/code-of-conduct')

client.run(os.getenv('TOKEN'))
