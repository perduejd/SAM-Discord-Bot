import discord
from discord.ext import commands
import yt_dlp
intents = discord.Intents.default()
intents.message_content = True
intents.typing = True
intents.presences = True


# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event: Welcomes a member when they join the guild
@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1163910076311023729)
    if channel:
        welcome_message = f'Welcome to the server, {member.mention}!'
        await channel.send(welcome_message)

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your Discord bot!')

# Command: !join, bot joins the voice channel the author is in
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        voice_channel = await channel.connect()
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

# Command: !leave, bot leaves the voice channel it is in
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not connected to a voice channel.")

@bot.command()
async def play(ctx, url):
    await play_music(ctx, url)


async def play_music(ctx, url):
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client  # Get the voice client

    if voice_channel:
        if voice_client:
            # If the bot is already connected, play the music
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'opus',  # Attempt Opus format
                    'preferredquality': '192',
                }]
            }

            ydl = yt_dlp.YoutubeDL(ydl_opts)
            info = ydl.extract_info(url, download=False)
            #url = info['formats'][0]['url']
            url = info['url']

            voice_client.play(discord.FFmpegPCMAudio(url))
        else:
            # If the bot is not connected, connect and play the music
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'opus',  # Attempt Opus format
                    'preferredquality': '192',
                }]
            }

            ydl = yt_dlp.YoutubeDL(ydl_opts)
            info = ydl.extract_info(url, download=False)
            #url = info['formats'][0]['url']
            url = info['url']

            # Connect to the voice channel
            voice_client = await voice_channel.connect()
            voice_client.play(discord.FFmpegPCMAudio(url))
    else:
        await ctx.send("You need to be in a voice channel to use this command.")


# Command: !pause
@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client

    if voice_client and voice_client.is_playing():
        voice_client.pause()
        await ctx.send('Song paused.')
    elif voice_client and voice_client.is_paused():
        await ctx.send('The song is already paused.')
    else:
        await ctx.send('No song is playing.')


# Command: !resume
@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client

    if voice_client and voice_client.is_paused():
        voice_client.resume()
        await ctx.send('Song resumed.')
    elif voice_client and voice_client.is_playing():
        await ctx.send('The song is already playing.')
    else:
        await ctx.send('No song is paused.')


# WILL NEED TO IMPLEMENT THIS AT THE END ONCE ALL OF OUR COMMANDS ARE COMPLETED AND FULLY FUNCTIONAL
#help command: !help  
async def help(ctx):
    help_embed = discord.Embed(
        title='SAM Bot Commands',
        description='Current List of available commands:',
        color=discord.Color.blue()
    ) # Bot commands and their purposes of the Server
    help_embed.add_field(name='!hello', value='Welcomes user to the channel.', inline=False) # For !command enter the command and for 'Description enter what the command does'
    help_embed.add_field(name='!join', value='Joins voice channel.', inline=False)
    help_embed.add_field(name='!leave', value='Leaves voice channel.', inline=False)
    help_embed.add_field(name='!play', value='Play a song followed by a URL.', inline=False)
    help_embed.add_field(name='!pause', value='Pauses the current song playing.', inline=False)
    help_embed.add_field(name='!resume', value='Resumes the current song paused.', inline=False)
    await ctx.send(embed=help_embed)


# Run the bot with your token
bot.run('MTE2MzkwODk0MzIxNTYwNzgwOA.GWH3bK.9y-b9XVIRtdX7DYiMwuzIr-9UnM-ag2D-wgFcE')
