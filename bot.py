import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
# the Oauth2 token for your bot user from the .env file
token = os.getenv('DISCORD_TOKEN')
# guild is what we would refer to as server
my_guild = os.getenv('DISCORD_GUILD')

# this instantiates a discord bot, which is a subclass of the discord Client class
# command_prefix determines what each command needs to start with
# Example: !test -> calls the test command
bot = commands.Bot(command_prefix='!')

@bot.command(name='linkedin', help='Responds with a link to the fellows google sheet')
async def linked_in_list(ctx):
	response = f'Here is the list of fellows linked in:'
	print("Someone is asking for the linkedin list...")
	await ctx.send(response)

bot.run(token)


