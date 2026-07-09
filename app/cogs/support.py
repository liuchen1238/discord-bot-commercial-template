"""Support ticket / feedback commands."""
import discord
from discord import app_commands
from discord.ext import commands

from app.services.notification_service import NotificationService


class SupportCog(commands.Cog, name="Support"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.notification_service = NotificationService()

    @app_commands.command(name="feedback", description="回報問題或建議給開發團隊")
    async def feedback(self, interaction: discord.Interaction, message: str) -> None:
        await self.notification_service.notify_developers(
            f"[Feedback] guild={interaction.guild_id} user={interaction.user.id}: {message}"
        )
        await interaction.response.send_message("感謝你的回饋！", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SupportCog(bot))
