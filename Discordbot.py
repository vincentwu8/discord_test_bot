import discord
import random
from discord import guild
from discord import embeds
from discord import message
from typing import ValuesView
from discord.ext import commands
import os

#from help_cog import help_cog
#from music_cog import music_cog
from discord.ext.commands.core import has_guild_permissions

async def send_message(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '!':
            user_message= user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.command()
    async def poll(ctx,*,message):
        emb = discord.Embed(title=" POLL ", description=f"{message}")
        mes = await ctx.channel.send(embed=emb)
        await mes.add_raction('👍')
        await mes.add_raction('👎')
        await mes.add_reaction('💦')

    client.run(TOKEN)

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'yuumi':
        return 'cummies'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == '!help':
        return 'stfu retard'
    
    if p_message == 'ching chong':
        return 'racist ass mfer frfr'
