import discord
from discord.ext import commands
from discord import app_commands
from assets.fightfs import *
from config import *

class Buttons(discord.ui.View):
	def __init__(self, provoker, victim, timeout=180):
		super().__init__(timeout=timeout)
		self.v = victim
		self.a = provoker
		self.turn = self.a
		self.vh = 100
		self.ah = 100
		self.damage = 0
		if victim.id == BOT_ID:
			print("amogooss")
		self.gameOver = False
	@discord.ui.button(label="attack", style=discord.ButtonStyle.blurple)
	async def my_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		try:
			if not self.gameOver:
				if interaction.user == self.turn:
					if self.turn == self.a:
						#attacker attacks victim
						self.vh, self.damage = atk(self.vh,1)
					else:
						#victim attacks attacker
						self.ah, self.damage = atk(self.ah,1)
					death, who = checkdead(self.a,self.ah,self.v,self.vh)
					if death:
						await interaction.response.edit_message(content=f"{who.mention} dead af")
						s.append = True
						self.gameOver = True
					else:
						self.turn = turnmgr(self.a,self.v,self.turn)
						await interaction.response.edit_message(content=display(self.a,self.ah,self.v,self.vh,self.turn,self.damage))
			else:
				button.disabled = True
		except Exception as e:
			print(e)
	@discord.ui.button(label="run", style=discord.ButtonStyle.red)
	async def my_button2(self, interaction: discord.Interaction, button: discord.ui.Button):
		if interaction.user == self.a or interaction.user == self.v:
			await interaction.response.edit_message(content=f"{interaction.user} is a LOSOR")
			button.disabled = True
			self.gameOver = True

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def fight(self, ctx, user: discord.User):
		try:
			await ctx.send(f"{user.mention} you are being fought", view=Buttons(user,ctx.author))
		except Exception as e:
			print(e)

	@app_commands.command(name="fight", description = "lets you fight someone")
	async def slashfight(self, interaction: discord.Interaction, user: discord.User):
		try:
			await interaction.response.send_message("")
		except Exception as e:
			print(e)

async def setup(bot):
	await bot.add_cog(Fun(bot), guilds = [discord.Object(1021957998727401522), discord.Object(993531972402040902)])
