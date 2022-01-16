import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix = '%')
token = 'TOKEN'

ydl_opts = { # Dictionary Containing settings for YT_DL
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('SoundBoard Ready!'))
    print('Bot is online')

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

@client.command()
async def joinChannel(ctx, *, given_name):
    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()

@client.command()
async def move(ctx, *, given_name):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

    channel = discord.utils.get(ctx.guild.channels, name=given_name)
    await channel.connect()

@client.command()
async def play(ctx, *, url):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

@client.command()
async def kill(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('kill.mp3'))

@client.command()
async def nfl(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('nfl.mp3'))

@client.command()
async def fries(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('fries.mp3'))

@client.command()
async def amogus(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('amogus.m4a'))

@client.command()
async def bruh(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('bruh.mp3'))

@client.command()
async def dababy(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('dababy.m4a'))   

@client.command()
async def dweeb(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('dweeb.mp3'))
    
@client.command()
async def save_slot(ctx, *, url): 
    song_there = os.path.isfile("song.mp3")
    
    if song_there == True:
        os.remove("song.mp3")

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

@client.command()
async def saved(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    voice.play(discord.FFmpegPCMAudio('song.mp3'))

client.run(token)
