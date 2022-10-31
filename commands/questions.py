import discord
from discord import app_commands
from discord.ext import commands

class Questions(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def sync(self,ctx) -> None:
		print("called")
		try:
			fmt = await ctx.bot.tree.sync(guild=ctx.guild)
			await ctx.send(f"synced {len(fmt)} commands")
		except Exception as e:
			print(e)



	@app_commands.command(name="questions", description="questions form")
	async def questions(self, interaction: discord.Interaction, question: str):
		await interaction.response.send_message('Answered')



async def setup(bot):
	await bot.add_cog(Questions(bot), guilds = [discord.Object(1021957998727401522), discord.Object(993531972402040902)])
