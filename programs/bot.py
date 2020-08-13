from discord.ext import commands
import jrlib
import random
import discord

bot = commands.Bot(command_prefix='~', case_insensitive=True)
bot.remove_command('help')

# Variables

eggcount = 0
wordcount = 0
diceCount = 0

# Ping-pong stuff

@bot.command()
async def ping(ctx):
    # This tests latency
    await ctx.send(f"Pong! (latency {bot.latency})")

@bot.command()
async def pong(ctx):
    # This confuses the bot
    await ctx.send(f"Po- wait what?")

# Other

@bot.command()
async def help(ctx):
    # Basic help command
    help_menu = "ping - Test bot latency"\
                "\n help - Opens the help menu"\
                "\n captcha - Test if you're talking with a bot"\
                "\n word [length] - Makes a new word with the length of word provided"\
                "\n egg - EGG"\
                "\n dice [sides] - Rolls a dice!"\
                "\n inv - See the inventory of your server"
    embed = discord.Embed(title = "Help", description = help_menu)
    await ctx.send(embed = embed)

@bot.command()
async def captcha(ctx):
    # Makes sure you're talking with a human!
    await ctx.send(" ``beep boop i am not a bot`` ")

@bot.command()
async def word(ctx, length):
    global wordcount
    
    if length.isdigit():
        length = int(length)
        if length > 2000:
            await ctx.send(f'The number you have inputted is above the 2000 character limit.')
            return
        outputword = jrlib.generate_word(length)
        wordcount = wordcount + 1
        await ctx.send(outputword)
    elif length.lower() == "a number":
        await ctx.send(f'The string of text "a number" isn\'t a number ')
    else:
        await ctx.send(f"{length} isn't a number stupid")
    

    # Makes a random word for you!

@bot.command()
async def egg(ctx):
    # EGG
    global eggcount
    eggcount = eggcount + 1
    await ctx.send(":egg:")

@bot.command() 
async def dice(ctx, sides):
    global diceCount
    
    if sides.isdigit():
        sides = int(sides)
        if sides < 1:
            await ctx.send(f"Cannot roll a dice with sides that are less then one.")
            return
        output = random.randint(1, sides)
        diceCount = diceCount + 1
        await ctx.send(output)
    elif sides.lower() == "a number":
        await ctx.send(f'The string of text "a number" isn\'t a number ')
    else:
        await ctx.send(f"{sides} isn't a number stupid")
    # Rolls a Dice
    

# Inventory

@bot.command()
async def inv(ctx):
    # Server's inventory
    global diceCount
    global eggcount
    global wordcount

    inv_menu = f"{eggcount} eggs"\
               f"\n {diceCount} dice thrown"\
               f"\n {wordcount} words generated"
    embed = discord.Embed(title = "Inventory", description = inv_menu)
    await ctx.send(embed = embed)

file = open("token.txt")  
token = file.read()
bot.run(token)