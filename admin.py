from discord import Member
from typing import List
from csv import DictWriter
from os import mkdir

def generate_csv(members: List[Member]):
  mkdir("output")
  filename = "output/test.csv"
  file = open(filename, "w")
  fields = ["Display Name", "Nickname"]
  writer = DictWriter(file, fieldnames=fields)
  writer.writeheader()
  writer.writerows(list(map(lambda m: dict({"Display Name": m.display_name, "Nickname": m.nick if m.nick is not None else "None" }), filter(lambda m: not m.bot, members))))
  file.close()