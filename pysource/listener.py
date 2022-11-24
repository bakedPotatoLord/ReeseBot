import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import config

token = config.TOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='./', intents=intents)

@client.event
async def on_message_delete(message):
	print("how tf does this work")

client.run(token)


