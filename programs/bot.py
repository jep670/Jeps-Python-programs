from discord.ext import commands
import numpy as np
import jrlib
import random
import discord
import signal
import sys
import os
import pickle


bot = commands.Bot(command_prefix='~', case_insensitive=True)
bot.remove_command('help')

# Variables

eggcount = 0
wordcount = 0
diceCount = 0

if os.path.exists("inventories.pkl"):
    file = open("inventories.pkl", "rb")
    inventories = pickle.load(file)
    file.close()
else:
    inventories = {}

# Functions


async def guide(ctx):
    guide_menu = '*For command help, use the `~help` command*'\
        "\n Chapters"\
        "\n 1. *Crafting*"\
        "\n 2. *Shop*"\
        "\n 3. *Getting materials*"
    crafting_menu = '*All crafting recipies*'\
        "\n *Crafting Table* - 10 wood."\
        "\n *Furnace* - 20 stone, 3 coal."\
        "\n *Anvil* - 2 iron bars, 10 wood."\
        "\n *Axe, 25* - 10 wood, 10 stone (requires a Crafting Table)."\
        "\n *Pickaxe, 25* - 10 wood, 10 stone (requires a Crafting Table)."\
        "\n *Iron Bar* - 4 iron ore, 3 coal (requires a furnace)"\
        "\n *Iron Axe, 25 - 10 wood, 3 iron bars (requires an anvil)"\
        "\n *Iron Pickaxe, 25 - 10 wood, 3 iron bars (requires an anvil)"
    shop_menu = "*What you can buy at the shop*"\
        "\n *Axe, 25* - 100 gold."\
        "\n *Pickaxe, 25* - 100 gold."\
        "\n *Guide* - 25 gold."
    matierials_menu = "*Where & how to get resources*"\
        "\n *Stone* - Use a pickaxe to get Stone."\
        "\n *Wood* - Use an axe to get Wood."\
        "\n *Coal* - Use a pickaxe to get Coal."\
        "\n *Iron Ore* - Use a Pickaxe to get Iron Ore."
    guide_embed = discord.Embed(title="Guide", description=guide_menu)
    crafting_embed = discord.Embed(title="Crafting", description=crafting_menu)
    shop_embed = discord.Embed(title="Shop", description=shop_menu)
    matierials_embed = discord.Embed(
        title="Materials",
        description=matierials_menu)
    await ctx.send(embed=guide_embed)
    await ctx.send(embed=crafting_embed)
    await ctx.send(embed=shop_embed)
    await ctx.send(embed=matierials_embed)


async def mine(ctx, inventory, level):
    if level == 1:
        ores = ["Stone", "Coal", "Iron Ore"]
        chance = [0.50, 0.45, 0.05]
    elif level == 2:
        ores = ["Stone", "Coal", "Iron Ore", "Copper Ore"]
        chance = [0.25, 0.25, 0.45, 0.05]
    elif level == 3:
        ores = ["Coal", "Iron Ore", "Copper Ore", "Gold Ore"]
        chance = [0.4, 0.25, 0.25, 0.05]
    elif level == 4:
        ores = ["Coal", "Copper Ore", "Gold Ore", "Diamond Ore"]
        chance = [0.4, 0.25, 0.25, 0.1]
    # content coming soon
    quantity = np.random.choice([2, 3], 1, [0.9, 0.1])[0]
    output = np.random.choice(ores, 1, chance)[0]
    give(inventory, output, quantity)
    give(inventory, "Stone")
    await ctx.send(f"You got {quantity} {output}s!")


def signal_handler(signal, frame):
    print("Saving dictionary...")
    file = open("inventories.pkl", "wb")
    pickle.dump(inventories, file)
    file.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Startup complete")


def give(inventory, item, quantity=1):
    if item not in inventory:
        inventory[item] = 0
    inventory[item] = inventory[item] + quantity


def remove(inventory, item, quantity=1):
    inventory[item] = inventory[item] - quantity
    if inventory[item] < 1:
        try:
            del inventory[item]
        except KeyError:
            return True


async def craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts=[]):
    """Takes inventory, verifies and removes items in input dictionary, verifies catalysts, and gives items in output dictionary."""
    has_items = True
    for catalyst in catalysts:
        if catalyst not in inventory:
            has_items = False
    for item in input:
        if item in inventory:
            if not inventory[item] >= input[item]:
                has_items = False
        else:
            has_items = False
    if has_items:
        for item in input:
            remove(inventory, item, input[item])
        for item in output:
            give(inventory, item, output[item])
        await ctx.send(success_msg)
    else:
        await ctx.send(fail_msg)


# Stands for "Dictionary 2 Inventory string"
def D2IS(inventory):
    inv_str = ""
    for item in inventory:
        inv_str = inv_str + f"**x{inventory[item]}** {item} \n"
    return inv_str


def generate_inv(member):
    if member.id not in inventories:
        inventories[member.id] = {}
        give(inventories[member.id], "Gold", 500)
        give(inventories[member.id], "Guide")
        give(inventories[member.id], "Starter Sword")
        give(inventories[member.id], "Starter Shield")
        give(inventories[member.id], "Axe", 50)
        give(inventories[member.id], "Pickaxe", 50)
        return True
    else:
        return False


@bot.command()
async def ping(ctx):
    # This tests latency
    await ctx.send(f"Pong! (latency {bot.latency})")


@bot.command()
async def pong(ctx):
    # This confuses the bot
    await ctx.send(f"Po- wait what?")


@bot.command()
async def help(ctx):
    # Basic help command
    help_menu = "  `ping` - Test bot latency"\
                "\n  `help` - Opens the help menu"\
                "\n  `captcha` - Test if you're talking with a bot"\
                "\n  `word` [length] - Makes a new word with the length of word provided"\
                "\n  `egg` - EGG"\
                "\n  `dice` [sides] - Rolls a dice!"\
                "\n  `count` - See the amount of times you used the commands (server wide)"
    embed = discord.Embed(
        title="Help, page 1 (prefix ~)",
        description=help_menu)
    rpg_help_menu = "`init` - Creates an inventory! Must use this command before anything else."\
        "\n  `inv` (@user) - Open your inventory, or another user's inventory."\
        "\n  `rm` [item] (quantity) - Removes an item from your inventory"\
        "\n  `use` [item] - Use an item"\
        "\n  `craft` [item] - Craft an item"\
        "\n  `shop` [item] - Buy an item"
    RPG_embed = discord.Embed(
        title="Help, page 2 (prefix ~)",
        description=rpg_help_menu)
    await ctx.send(embed=embed)
    await ctx.send(embed=RPG_embed)


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
async def count(ctx):
    # Server's inventory
    global diceCount
    global eggcount
    global wordcount

    cnt_menu = f"{eggcount} eggs"\
               f"\n {diceCount} dice thrown"\
               f"\n {wordcount} words generated"
    embed = discord.Embed(title="Command Count", description=cnt_menu)
    await ctx.send(embed=embed)

# RPG stuff


@bot.command()
async def init(ctx):
    if generate_inv(ctx.message.author):
        await ctx.send("Initialisation complete! If you're ever stuck or lost, do `~use Guide`. ")
        return
    await ctx.send("You already have an inventory!")


@bot.command()
async def inv(ctx, member: discord.User = None):
    # User inventory
    if member:
        id = member.id
    else:
        id = ctx.message.author.id
        member = ctx.message.author

    inv_str = D2IS(inventories[id])
    embed = discord.Embed(title="Inventory", description=inv_str)
    await ctx.send(f"{member.mention}'s inventory", embed=embed)


@bot.command()
async def rm(ctx, item, quantity="1"):
    # Removes an item
    if quantity.isdigit():
        quantity = int(quantity)
        if quantity < 0:
            await ctx.send(f"Cannot remove negative items.")
            return
    elif quantity.lower() == "a number":
        await ctx.send(f'The string of text "a number" isn\'t a number ')
    else:
        await ctx.send(f"{quantity} isn't a number stupid")
    id = ctx.message.author.id
    inventory = inventories[id]
    if remove(inventory, item, quantity):
        await ctx.send("That item doesn't exist!")
        return
    await ctx.send(f"{quantity} {item}(s) have been removed from your inventory")


@bot.command()
async def use(ctx, item):
    id = ctx.message.author.id
    inventory = inventories[id]
    if not inventory.get(item):
        await ctx.send(f"You don't have {item}!")
        return
    if item == "Axe":
        await ctx.send("this is broken for now")
    elif item == "Pickaxe":
        await mine(ctx, inventory, 1)
        remove(inventory, "Pickaxe")
    elif item == "Iron Pickaxe":
        await mine(ctx, inventory, 2)
        remove(inventory, "Iron Pickaxe")
    elif item == "Copper Pickaxe":
        await mine(ctx, inventory, 3)
        remove(inventory, "Copper Pickaxe")
    elif item == "Gold Pickaxe":
        await mine(ctx, inventory, 4)
        remove(inventory, "Gold Pickaxe")
    elif item == "Guide":
        await guide(ctx)
    elif item == "Crafting Table":
        await ctx.send("You can't use the crafting table directly, but you can use it in crafting. Do `~use Guide` for more info.")
    elif item == "Furnace":
        await ctx.send("You can't use the Furnace directly, but you can use it in crafting. Do `~use Guide` for more info.")
    else:
        await ctx.send(f"You can't use {item}")


@bot.command()
async def craft(ctx, item):
    id = ctx.message.author.id
    inventory = inventories[id]
    if item == "Crafting Table":
        input = {"Wood": 10}
        output = {"Crafting Table": 1}

        success_msg = "Crafted a crafting table!"
        fail_msg = "You lack the required resources! You need 10 Wood."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output)

    elif item == "Axe":
        input = {"Wood": 10, "Stone": 10}
        output = {"Axe": 25}
        catalysts = ["Crafting Table"]

        success_msg = "Made 25 Axes!"
        fail_msg = "You lack the required resources! You need 10 Wood, 10 Stone and a Crafting Table."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Pickaxe":
        input = {"Wood": 10, "Stone": 10}
        output = {"Pickaxe": 25}
        catalysts = ["Crafting Table"]

        success_msg = "Made 25 Pickaxes!"
        fail_msg = "You lack the required resources! You need 10 Wood, 10 Stone and a Crafting Table"

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Furnace":
        input = {"Stone": 20, "Coal": 3}
        output = {"Furnace": 1}
        catalysts = ["Crafting Table"]

        success_msg = "Made a Furnace!"
        fail_msg = "You lack the required resources! You need 20 Stone, 3 Coal and a Crafting Table."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Anvil":
        input = {"Iron Bar": 2, "Wood": 10}
        output = {"Anvil": 1}
        catalysts = ["Crafting Table"]

        success_msg = "Made an Anvil!"
        fail_msg = "You lack the required resources! You need 10 Wood, 2 Iron Bars and a Crafting Table."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Iron Bar":
        input = {"Iron Ore": 4, "Coal": 3}
        output = {"Iron Bar": 1}
        catalysts = ["Furnace"]

        success_msg = "Forged an Iron Bar!"
        fail_msg = "You lack the required resources! You need 4 Iron Ore, 3 Coal and a Furnace."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Iron Pickaxe":
        input = {"Iron Bar": 3, "Wood": 10}
        output = {"Iron Pickaxe": 25}
        catalysts = ["Anvil"]

        success_msg = "Assembled 25 Iron Pickaxes!"
        fail_msg = "You lack the required resources! You need 10 Wood, 3 Iron Bars and an Anvil."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)

    elif item == "Iron Axe":
        input = {"Iron Bar": 3, "Wood": 10}
        output = {"Iron Axe": 25}
        catalysts = ["Anvil"]

        success_msg = "Assembled 25 Iron Axes!"
        fail_msg = "You lack the required resources! You need 10 Wood, 3 Iron Bars and an Anvil."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output, catalysts)
    else:
        await ctx.send(f"{item} can't be crafted.")


@bot.command()
async def shop(ctx, item):
    id = ctx.message.author.id
    inventory = inventories[id]
    if item == "Axe":
        input = {"Gold": 100}
        output = {"Axe": 25}

        success_msg = "Craf- I mean Bought an Axe!"
        fail_msg = "You lack the required funds! You need 100 Gold."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output)

    elif item == "Pickaxe":
        input = {"Gold": 100}
        output = {"Pickaxe": 25}

        success_msg = "Bought a Pickaxe!"
        fail_msg = "You lack the required funds! You need 100 Gold."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output)

    elif item == "Guide":
        input = {"Gold": 25}
        output = {"Guide": 1}

        success_msg = "Bought a Guide! You can use it with `~use Guide` (items are case sensitive.)"
        fail_msg = "You lack the required funds! You need 25 Gold."

        await craft_item(ctx, inventory, fail_msg, success_msg, input, output)
    else:
        await ctx.send(f"{item} isn't for sale.")
file = open("token.txt")
token = file.read()
bot.run(token)
