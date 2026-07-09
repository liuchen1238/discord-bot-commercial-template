"""Slash commands contributed by the example plugin."""
import discord
from discord import app_commands
from discord.ext import commands


class ExampleCog(commands.Cog, name="Example Plugin"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="hello", description="範例外掛指令")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello from the example plugin!")
