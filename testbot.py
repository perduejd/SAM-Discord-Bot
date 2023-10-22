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