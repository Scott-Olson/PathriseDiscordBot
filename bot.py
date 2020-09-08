import os
import asyncio
import discord
import requests
# import beautifulsoup4

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
GUILD = bot.fetch_guild(751588559693152297)
# greetings for members and channel updates
class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send('Welcome {0.mention}.'.format(member))

# Pathrise code templates
class Templates(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


# broadcast the fellows linked in list
cur_list = "https://docs.google.com/spreadsheets/d/1clZOTGUNFC6Osf5OIK2S5kGsr2IzhkidcZ9FBe88kdk/"
short_link = "https://bit.ly/2ZcIzls"
@bot.command(name='linkedin', help='Responds with a link to the fellows google sheet')
async def linked_in_list(ctx):
	li_chan = bot.get_channel(752050305234894938)
	response = f"Here is the official compiled list of fellow's LinkedIn:  {short_link} \nIf you are not on the list, please feel free to add yourself! \n Please also check out #linkedin-plug for other users to connect with."

	print("Someone is asking for the linkedin list...")
	await ctx.send(response)

# easy leetcode problem
@bot.command(name='easy', help='Returns a link to a leetcode easy.')
async def get_easy(ctx):
	response = f'Try this leetcode easy! LINK'
	await ctx.send(response)

# med leetcode problem
@bot.command(name='medium', help='Returns a link to a leetcode medium.')
async def get_medium(ctx):
	response = f'Try this leetcode medium! LINK'
	await ctx.send(response)

# hard leetcode problem
@bot.command(name='hard', help='Returns a link to a leetcode hard.')
async def get_hard(ctx):
	get_leetcode_question('hard')
	response = f'Try this leetcode hard! LINK'
	await ctx.send(response)

# random leetcode problem
@bot.command(name='random', help='Returns a link to a random leetcode.')
async def get_random(ctx):
	# get_leetcode_question('')
	response = f'Try this random leetcode! LINK'
	await ctx.send(response)



"""
Because leetcode doesn't have an easy access API to recieve the problems
I will attempt to get the problems via requests and beautifulsoup by hitting these https gets


https://leetcode.com/problems/random-one-question/all
https://leetcode.com/problems/random-one-question/all/?difficulty=Easy
https://leetcode.com/problems/random-one-question/all/?difficulty=Medium
https://leetcode.com/problems/random-one-question/all/?difficulty=Hard
"""
def get_leetcode_question(dif: str):
	# build the url for the request

	r = requests.get('https://leetcode.com/problems/random-one-question/all/', params = {'difficulty=': dif}, allow_redirects = True)
	print(r.url)
	print(r.text)
	# print(r.content)





bot.add_cog(Greetings(bot))
bot.add_cog(Templates(bot))
bot.run(token)


