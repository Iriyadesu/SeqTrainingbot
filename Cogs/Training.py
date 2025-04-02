import discord
from discord.ext import commands
from discord import app_commands

from Views import TrainingDropdown
class Training(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="request_training",
            description="Command to open the training request modal."
    )

    async def request_training(self,interaction: discord.Interaction):
        """Command to open the training request modal."""
        await interaction.response.send_message("Select your training type:", view=TrainingDropdown())

async def setup(bot):
    await bot.add_cog(Training(bot))