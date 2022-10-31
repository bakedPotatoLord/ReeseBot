import discord
try:
	import config
except Exception as e:
	print("you need to make a config.py containing a TOKEN variable and a APP_ID variable")
	print(e)
import asyncio
import os
from discord.ext import commands

OK = True

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=",", intents=intents, application_id=config.APP_ID)

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


@bot.event
async def on_ready():
	global OK
	if OK:
		print(f'Welcome aboard captain, all systems {OKGREEN}online{ENDC}\n{HEADER}------------------------------------------{ENDC}')
	else:
		print(f'Welcome aboard captain,{WARNING} some systems are {FAIL}OFFLINE{ENDC}\n{HEADER}------------------------------------------{ENDC}')

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if message.author == bot.user:
		return
	if message[:2] == './':
		return
	#code

async def load():
	global OK
	for file in os.listdir("./commands"):
		if file[-3:] == ".py":
			try:
				await bot.load_extension(f'commands.{file[:-3]}')
				print(f"{file[:-3]} {OKGREEN}Online{ENDC}")
			except Exception as e:
				OK = False
				print(f"{file[:-3]} {FAIL}OFFLINE{ENDC} > {e}")
async def main():
	await load()
	await bot.start(config.TOKEN)

asyncio.run(main())

