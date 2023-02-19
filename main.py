import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

#def run_cat_bot():
#    intents = discord.Inents.default()
#    intents.message_content = True
#    bot = discord.Bot(intents=intents)
#    
#    @bot.event
#    async def on_ready():
#        print(f'{bot.user} is now running!')
#        
#    @client.event
#    async def on_message(message):
#        if message.author = bot.user:
#            return
#        
#        username = str(message.author)
#        user_message = str(message.content)
#        channel = str(message.channel)

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="shop")
@app_commands.describe(action='What would you like to do?')
@app_commands.choices(action=[
        discord.app_commands.Choice(name='Go to Inventory', value = 1),
        discord.app_commands.Choice(name='Go to Shop', value = 2),

])
async def shop(interaction: discord.Interaction, action: discord.app_commands.Choice[int]):
    await interaction.response.send_message(f"Action Choosen: {action.name}")
#Display_pets:Optional[bool], Display_items:Optional[bool]):
    #display pets and items

    #use if-statements to determine what they choose to buy
    #within if statement, add that item to the specific list and subtract the money from the wallet

    #Ask if they would like to continue shopping