import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
import time

TOKEN = 'MTA3NjYzNDM1MzAxMjA0NzkzNA.GIH7a-.fwOG3Wn6nW5bRFAaulTju_yLQ0F-8uLvp0XzsU'
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#Cat
Hunger = True
Thirst = True
Happiness = 3
Illness = False

#Global for server
Inventory = []
Wallet = 0


class MyView(discord.ui.View): 
    @discord.ui.button(label='Pet the Cat', style=discord.ButtonStyle.primary)
    async def petting(self, interaction:discord.Interaction, button):
        button.disabled = True
        await interaction.response.edit_message(content='Done patting!',view=self)

@bot.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

""" @bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message)
    if message.author == bot.user:
        return
    if user_message.lower() == 'hello':
        await message(f'Helloo {username}!')
    elif user_message.lower == 'hello cat':
        await message(f'Helloo {username}!')
    elif user_message.lower == 'meow':
        await message(f'Meoww!')
    elif user_message.lower == 'i love you':
        await message(f'Purr!')
    elif user_message.lower == 'i love you cat':
        await message(f'Purr!') """

@bot.tree.command(name="shop")
@app_commands.describe(action='What would you like to buy?')
@app_commands.choices(action=[
        discord.app_commands.Choice(name='Tuna for $50', value = 1),
        discord.app_commands.Choice(name='Kibble for $50', value = 2),
        discord.app_commands.Choice(name='Water for $25', value = 3),
        discord.app_commands.Choice(name='Milk for $50', value = 4)])
async def shop(interaction: discord.Interaction, action: discord.app_commands.Choice[int]):
    if action.value == 1:
        Inventory.append('Tuna')
        #Wallet -= 50
        await interaction.response.send_message('Tuna has been added to the inventory. :)')
    elif action.value == 2:
        Inventory.append('Kibble')
        #Wallet -= 50
        await interaction.response.send_message('Kibble has been added to the inventory. :)')
    elif action.value == 3:
        Inventory.append('Water')
        #Wallet -= 25
        await interaction.response.send_message('Water has been added to the inventory. :)')
    elif action.value == 4:
        Inventory.append('Milk')
        #Wallet -= 50
        await interaction.response.send_message('Milk has been added to the inventory. :)')
    else:
        await interaction.response.send_message('Not Available')

@bot.tree.command(name="feed_cat")
@app_commands.choices(option=[
        discord.app_commands.Choice(name='Tuna', value = 1),
        discord.app_commands.Choice(name='Kibble', value = 2),
        discord.app_commands.Choice(name='Water', value = 3),
        discord.app_commands.Choice(name='Milk', value = 4), 
        discord.app_commands.Choice(name='Nothing', value = 5)])
async def feed_cat(interaction: discord.Interaction, option: discord.app_commands.Choice[int]):
    if option.value != 5:
            await interaction.response.send_message(f"Your cat has been fed, {option.name}")
    else:
        await interaction.response.send_message("You starved your cat")

@bot.tree.command(name="get_inventory")
async def get_inventory(interaction: discord.Interaction):
    await interaction.response.send_message(f'Inventory: {Inventory}\nWallet: ${Wallet}')

@bot.tree.command(name="display_cat_info")
async def display_cat_info(interaction: discord.Interaction):
    await interaction.response.send_message(f'Happiness Level: {Happiness}\nHunger: {Hunger}\nThirst: {Thirst}\nIllness: {Illness}')

@bot.tree.command(name="pet_cat")
async def pat_cat(interaction: discord.Interaction, pet: bool):
    await interaction.response.send_message("Patting the cat...", view=MyView())

bot.run(TOKEN)