import discord
try:
	import config
except Exception as e:
	print("you need to make a config.py containing a TOKEN variable, LOGID variable and a APP_ID variable")
	print(e)
import asyncio
import os
from discord.ext import commands
from threading import Thread
import asyncio

OK = True

intents = discord.Intents.all()

bot = discord.Client(intents=intents)
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

try:
	from assets.tiktokapi import *
	print(f"TikTokApi {OKGREEN}Online{ENDC}")
except Exception as e:
	OK = False
	print(f"TikTokApi {FAIL}OFFLINE{ENDC} > {e}")

def processLink(message,loop):
	try:
		start = 0
		for dex in range(0,len(message.content)):
			if message.content[dex:5+dex] == "https":
				start = dex
		url = message.content[start:]
		vid, ff = video(url)
		loop.create_task(sendVideo(message,vid,ff))
	except Exception as e:
		print(e)

async def sendVideo(message,vid,ff):
			try:
				await message.reply(file=vid)
			except:
				print("failed")
				await message.channel.send(file=vid)
			os.system(f"rm finished{ff}.mp4")



@bot.event
async def on_ready():
	global OK
	if OK:
		print(f'Welcome aboard captain, all systems {OKGREEN}online{ENDC}\n{HEADER}------------------------------------------{ENDC}')
	else:
		print(f'Welcome aboard captain,{WARNING} some systems are {FAIL}OFFLINE{ENDC}\n{HEADER}------------------------------------------{ENDC}')
	try:
		compressforever = Thread(target=compress_forever)
		compressforever.start()
	except Exception as e:
		print(e)

@bot.event
async def on_message_delete(message):
	print("DELETION")
	try:
		if message.channel.id != config.LOGID:
			log = bot.get_channel(config.LOGID)
			await log.send(f"{message.author.display_name}:\n{message.content}\nattachments: {message.attachments}")
	except Exception as e:
		print(e)
@bot.event
async def on_message(message):
	try:
		if "https://" in message.content:
			#thing = asyncio.get_event_loop().create_task(processLink(message))
			print("VID FOUND")
			thread = Thread(target=processLink,args=(message,asyncio.get_event_loop(),))
			thread.start()
	except Exception as e:
		print(e)
	if bot.user.mentioned_in(message):
		print("pung")
		try:
			msg = await message.channel.fetch_message(message.reference.message_id)
			await on_message(msg)
		except Exception as e:
			print(e)
	await bot.process_commands(message)
	if message.author == bot.user:
		return
	if message[0] == ',':
		return
	#no on_message code beyond this point!

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

