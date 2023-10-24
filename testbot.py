import discord
from discord.ext import commands
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

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am your Discord bot!')

# Run the bot with your token
bot.run('MTE2MzkwODk0MzIxNTYwNzgwOA.GWH3bK.9y-b9XVIRtdX7DYiMwuzIr-9UnM-ag2D-wgFcE')



#Pause command: !pause
voice_channel = ctx.author.voice.channel

async def pause(ctx):
    voice_channel = ctx.author.voice.channel

    if voice_channel:
        voice_client = await voice_channel.connect()

        if voice_client.is_playing():
            voice_client.pause()
            await ctx.send('Current song playing paused.')
        else:
            await ctx.send('No song playing.')
        
        await voice_client.disconnect()


# Resume song command: !resume
async def resume(ctx):
    
    resume_text = "Resumes playing the current song."
    await ctx.send(resume_text)


#Skip command: !skip
async def skip(ctx):
    voice_channel = ctx.author.voice.channel

    if voice_channel:
        voice_client = await voice_channel.connect() #Connects to channel

        if voice_client.is_playing():
            voice_client.stop()
            await ctx.send('Skipped the current song playing.')
        else:
            await ctx.send('No song is playing.')

