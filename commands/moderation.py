import discord
from discord import app_commands
from discord.ext import commands
import os
from random import choice
import asyncio


def texts(file):
        with open(file) as f:
                lines = f.readlines()
                lines = [s.strip('\n') for s in lines]
                return choice(lines)

class Moderation(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.target = None
	@commands.Cog.listener()
	async def on_ready(self):
		pass


	@commands.Cog.listener()
	async def on_message_delete(message):
		print("triggered")

	@app_commands.command(name="nuke", description="deletes set amount of messages")
	@app_commands.checks.has_permissions(manage_messages=True)
	async def slashnuke(self, interaction: discord.Interaction, amount: int, who: discord.User = None):
		def istarget(msg):
			return self.target== msg.author

		try:
			buff = 0
			amnt = 0
			msg = await interaction.response.send_message(f"deleting {amount} messages")
			await asyncio.sleep(1)
			amount += 1
			if who == None:
				await interaction.channel.purge(limit=amount)
			else:
				async for message in interaction.channel.history(limit=200):
					if message.author == who:
						amnt+=1
					buff+=1
					if amnt >= amount:
						buff -= amount
						break
				self.target = who
				await interaction.channel.purge(limit=amount+buff, check=istarget)
		except Exception as e:
			print(e)

async def setup(bot):
	await bot.add_cog(Moderation(bot), guilds = [discord.Object(1021957998727401522), discord.Object(993531972402040902)])
