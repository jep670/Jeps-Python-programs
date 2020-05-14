from discord.ext import commands
import jrlib
import random

bot = commands.Bot(command_prefix='~', case_insensitive=True)
bot.remove_command('help')

# Variables

carcount = 0
eggcount = 0
wordcount = 0
pingpongcount = 0

# Ping-pong stuff

@bot.command()
async def ping(ctx):
    # This tests latency
    await ctx.send(f"Pong! (latency {bot.latency})")

@bot.command()
async def pong(ctx):
    # This confuses the bot
    await ctx.send(f"Po- wait what?")

@bot.command()
async def pingpong(ctx):
    # This makes it so you play pingpong with the bot
    global pingpongcount
    pingpongcount = pingpongcount + 1
    await ctx.send(f":ping_pong:")

# Other

@bot.command()
async def Help(ctx):
    # Basic help command
    await ctx.send("``` Prefix: '~' \n \n Other \n help: Shows this message \n captcha: makes sure you're talking with a human \n egg: EGG \n nicecar: Give you a nice car! \n word: Makes a word for you! \n inv: Shows all of the objects collected in the server. \n \n Ping & Pong \n ping: Tests Latency of bot \n pingpong: Play pingpong with the bot! ```")

@bot.command()
async def captcha(ctx):
    # Makes sure you're talking with a human!
    await ctx.send(" ``beep boop i am not a bot`` ")

@bot.command()
async def word(ctx):
    global wordcount
    wordcount = wordcount + 1
    length = random.randint(1, 10)
    
    outputword = jrlib.generate_word(length)

    # Makes a random word for you!
    await ctx.send(outputword)

@bot.command()
async def egg(ctx):
    # EGG
    global eggcount
    eggcount = eggcount + 28
    await ctx.send(":egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg::egg:")

@bot.command()
async def nicecar(ctx):
    # Wow, nice car!
    global carcount  
    carcount = carcount + 1
    await ctx.send(" n||ice ca||r ")

# Inventory

@bot.command()
async def inv(ctx):
    # Server's inventory
    global carcount
    global eggcount
    global wordcount
    global pingpongcount
    await ctx.send(f"The server's inventory contains: ``` {eggcount} egg(s) \n {carcount} car(s) \n {wordcount} word(s) \n {pingpongcount} ping pong round(s) played with the bot. ```")

file = open("token.txt")  
token = file.read()
bot.run(token)