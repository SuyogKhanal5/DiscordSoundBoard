import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '%')
token = 'TOKEN'

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

client.run(token)
