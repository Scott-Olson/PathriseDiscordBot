import os
import asyncio
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
bot = commands.Bot(command_prefix = '!', case_insensitive = True, description = 'Pathrise SWE Bot')

# broadcast the fellows linked in list
@bot.command(name='linkedin', help='Responds with a link to the fellows google sheet')
async def linked_in_list(ctx):
	response = f'Here is the list of fellows linked in:'
	print("Someone is asking for the linkedin list...")
	await ctx.send(response)

# easy leetcode problem
@bot.command(name='easy', help='Returns a link to a leetcode easy.')
async def function(ctx):
	response = f'Try this leetcode easy! LINK'
	await ctx.send(response)

# med leetcode problem
@bot.command(name='medium', help='Returns a link to a leetcode medium.')
async def function(ctx):
	response = f'Try this leetcode medium! LINK'
	await ctx.send(response)

# hard leetcode problem
@bot.command(name='hard', help='Returns a link to a leetcode hard.')
async def function(ctx):
	response = f'Try this leetcode hard! LINK'
	await ctx.send(response)

# random leetcode problem
@bot.command(name='random', help='Returns a link to a random leetcode.')
async def function(ctx):
	response = f'Try this random leetcode! LINK'
	await ctx.send(response)

"""
https://leetcode.com/problemset/all
https://leetcode.com/problemset/all/?difficulty=Easy
https://leetcode.com/problemset/all/?difficulty=Medium
https://leetcode.com/problemset/all/?difficulty=Hard
"""

async def get_leetcode_question(difficulty: str):
	await

bot.run(token)


