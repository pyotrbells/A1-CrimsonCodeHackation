import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

bot = commands.Bot(command_prefic="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        sync = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="shop")
async def shop(interaction: discord.Interaction, Display_pets:Optional[bool], Display_items:Optional[bool]):
    #display pets and items

    #use if-statements to determine what they choose to buy
    #within if statement, add that item to the specific list and subtract the money from the wallet

    #Ask if they would like to continue shopping