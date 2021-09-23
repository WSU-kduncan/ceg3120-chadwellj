import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    meow = [
        'Im Independent',
        'Ive been good',
        'I make biscuits',
        'Cuddly',

    ]

    if message.content == 'orelse!':
        await message.channel.send(file=discord.File('givemetreats.png'))
    if message.content == 'reasonsfortreats!':
         response = random.choice(meow)
         await message.channel.send(response)

client.run(TOKEN)
