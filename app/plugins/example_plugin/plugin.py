"""Entry point for the example plugin, loaded by app.plugins.loader."""
from discord.ext import commands

from app.plugins.example_plugin.commands import ExampleCog


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExampleCog(bot))
