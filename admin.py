from discord import Member
from discord.ext import commands
from typing import List
from csv import DictWriter
import os

class NotAdminError(commands.CheckFailure):
    pass

def is_admin():
	async def predicate(ctx):
		if not ctx.author.guild_permissions.administrator:
			raise NotAdminError("Sorry, this information is need-to-know.")
		return True
	return commands.check(predicate)

def generate_csv(members: List[Member]) -> str:
	if not os.path.isdir("output"):
		os.mkdir("output")

	humans = filter(lambda m: not m.bot, members)
	readable_humans = map(lambda m: {
		"ID": m.id,
		"Name": m.name,
		"Display Name": m.display_name,
		"Joined At": m.joined_at,
	}, humans)

	filename = "output/compatriats.csv"
	fields = ["ID", "Name", "Display Name", "Joined At"]
	file = open(filename, "w")
	writer = DictWriter(file, fieldnames=fields)
	writer.writeheader()
	writer.writerows(readable_humans)
	file.close()

	return filename
