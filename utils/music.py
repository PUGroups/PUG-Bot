import asyncio
import os 
import discord
import youtube_dl
import random
from discord.ext import commands
from discord.ext import tasks
import time
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''
red = 0xF04747
green = 0x43B581
orange = 0xFAA61A

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def play(self, ctx, *, url):

     
        player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        try:
          ctx.voice_channel.disconnect()
        except:
          pass
        try:
          ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
          embed=discord.Embed(color=green)
          embed.add_field(name=":white_check_mark:", value=f"Now playing {player.title}", inline=False)
          await ctx.send(embed=embed)
        except Exception as e:
          print(e)
        
        
          
          

        
        try:
          while ctx.voice_client.is_playing():
            
            await asyncio.sleep(.1)
        
          await ctx.voice_client.disconnect()
        except:
          pass
        



    @commands.command()
    async def volume(self, ctx, volume: int):

        if ctx.voice_client is None:
            embed=discord.Embed(color=red)
            embed.add_field(name=":x:", value="Please use the `?play` command first.", inline=False)
            return await ctx.send(embed=embed)

        ctx.voice_client.source.volume = volume / 100
        embed=discord.Embed(color=green)
        embed.add_field(name=":white_check_mark:", value=f"Volume changed to {volume}", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self, ctx):
      try:
        await ctx.voice_client.disconnect()
      except:
        embed=discord.Embed(color=red)
        embed.add_field(name=":x:", value="Please join a voice channel and use the `?play` command first.", inline=False)
        await ctx.send(embed=embed)

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed=discord.Embed(color=red)
                embed.add_field(name=":x:", value="Please join a voice channel first.", inline=False)
                await ctx.send(embed=embed)
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(bot):
    bot.add_cog(Music(bot))