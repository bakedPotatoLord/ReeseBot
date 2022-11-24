import discord
from discord.ext import commands



class Buttons(discord.ui.View):
	def __init__(self, *, timeout=180):
		super().__init__(timeout=timeout)

	@discord.ui.button(label="clickme", style=discord.ButtonStyle.gray)
	async def my_button(self, interaction: discord.Interaction, button: discord.ui.Button):
		for button in self.children:
			button.disabled = True
		await interaction.response.edit_message(view=self)
class Clickme(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		pass

	@commands.command()
	async def click(self, ctx):
		print("Called")
		await ctx.send("Message wit a button", view=Buttons())

async def setup(bot):
	await bot.add_cog(Clickme(bot))
