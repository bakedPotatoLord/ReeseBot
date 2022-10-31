import discord
from discord import app_commands
from discord.ext import commands
import os
from random import choice

def texts(file):
        with open(file) as f:
                lines = f.readlines()
                lines = [s.strip('\n') for s in lines]
                return choice(lines)

class Fortunes(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@app_commands.command(name="8", description="The magic eightball")
	async def B(self, interaction: discord.Interaction, question: str):
		try:
			await interaction.response.send_message(texts("./assets/textFiles/8ball.8"))
		except Exception as e:
			print(e)


async def setup(bot):
	await bot.add_cog(Fortunes(bot), guilds = [discord.Object(1021957998727401522), discord.Object(993531972402040902)])
