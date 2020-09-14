from discord import Member
from typing import List
from csv import DictWriter
import os

def generate_csv(members: List[Member]):
  if not os.path.isdir("output"):
    os.mkdir("output")

  filename = "output/test.csv"
  fields = ["Display Name", "Nickname"]
  file = open(filename, "w")
  writer = DictWriter(file, fieldnames=fields)
  writer.writeheader()
  writer.writerows(list(map(lambda m: dict({"Display Name": m.display_name, "Nickname": m.nick if m.nick is not None else "None" }), filter(lambda m: not m.bot, members))))
  file.close()