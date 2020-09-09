import os
import asyncio
import discord
import requests
import problems
# import beautifulsoup4

from dotenv import load_dotenv
from discord.ext import commands

problems.update_problem_list()

load_dotenv()
# the Oauth2 token for your bot user from the .env file
# token = os.getenv('DISCORD_TOKEN')
token = os.environ.get('DISCORD_TOKEN')
# guild is what we would refer to as server
# my_guild = os.getenv('DISCORD_GUILD')
my_guild = os.environ.get('DISCORD_GUILD')

# this instantiates a discord bot, which is a subclass of the discord Client class
# command_prefix determines what each command needs to start with
# Example: !test -> calls the test command
bot = commands.Bot(command_prefix = '!', case_insensitive = True, description = 'Pathrise SWE Bot')

# broadcast the fellows linked in list
# cur_list = os.getenv('FELLOWS_LI_LIST')
cur_list = os.environ.get('FELLOWS_LI_LIST')

# short_link = os.getenv('SHORT_LINK')
short_link = os.environ.get('SHORT_LINK')

# bot_link = os.getenv('DISCORD_REPO')
bot_link = os.environ.get('DISCORD_REPO')

@bot.command(name = 'linkedin', help = 'Responds with a link to the fellows google sheet')
async def linked_in_list(ctx):
	li_chan = bot.get_channel(752050305234894938)
	response = f"Here is the official compiled list of fellow's LinkedIn:  {short_link} \nIf you are not on the list, please feel free to add yourself! \n Please also check out #linkedin-plug for other Discord users to connect with."

	print("Someone is asking for the linkedin list...")
	await ctx.send(response)

@bot.command(name = 'botinfo', help = 'Github page of the Discord bot. Feel free to contribute!')
async def bot_info(ctx):
	response = f'This is the repo of this bot: {bot_link} \n Feel free to contribute!'
	await ctx.send(response)

# easy leetcode problem
@bot.command(name = 'easy', help = 'Returns a link to a leetcode easy.')
async def get_easy(ctx):
	prob = problems.get_easy_problem()
	print(f'Giving them an easy one: {prob.title}')
	response = f"Here is a random easy problem to try!\n {prob.get_title()}: {prob.get_link()}"
	await ctx.send(response)

# med leetcode problem
@bot.command(name = 'medium', help = 'Returns a link to a leetcode medium.')
async def get_medium(ctx):
	prob = problems.get_medium_problem()
	print(f'Giving them a medium: {prob.title}')
	response = f"Here is a random medium problem to try!\n {prob.get_title()}: {prob.get_link()}"
	await ctx.send(response)

# hard leetcode problem
@bot.command(name = 'hard', help = 'Returns a link to a leetcode hard.')
async def get_hard(ctx):
	prob = problems.get_hard_problem()
	print(f'Giving them a hard: {prob.title}')
	response = f"Here is a random hard problem to try!\n {prob.get_title()}: {prob.get_link()}"
	await ctx.send(response)

# random leetcode problem
@bot.command(name = 'random', help = 'Returns a link to a random leetcode.')
async def get_random(ctx):
	prob = problems.get_random_problem()
	print(f'Random problem given: {prob.title}')
	response = f"Here is a random problem to try!\n {prob.get_title()}: {prob.get_link()}"
	await ctx.send(response)

# set the daily leetcode problem for the server
@bot.command(name = 'setdaily', help = '*in development* Used to set the daily problem for the server.')
async def set_daily(ctx):
	await ctx.send()


"""
Because leetcode doesn't have an easy access API to recieve the problems
I will attempt to get the problems via requests and beautifulsoup by hitting these https gets


https://leetcode.com/problems/random-one-question/all
https://leetcode.com/problems/random-one-question/all/?difficulty=Easy
https://leetcode.com/problems/random-one-question/all/?difficulty=Medium
https://leetcode.com/problems/random-one-question/all/?difficulty=Hard
"""


bot.run(token)


