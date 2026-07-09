"""Slash commands for viewing and managing guild subscriptions."""
import discord
from discord import app_commands
from discord.ext import commands

from app.services.billing_service import BillingService
from app.services.subscription_service import SubscriptionService


class BillingCog(commands.Cog, name="Billing"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.billing_service = BillingService()
        self.subscription_service = SubscriptionService()

    @app_commands.command(name="plan", description="查看目前伺服器的訂閱方案")
    async def plan(self, interaction: discord.Interaction) -> None:
        subscription = await self.subscription_service.get_for_guild(interaction.guild_id)
        plan_name = subscription.plan.name if subscription else "Free"
        await interaction.response.send_message(f"目前方案：**{plan_name}**")

    @app_commands.command(name="upgrade", description="取得升級訂閱的付款連結")
    async def upgrade(self, interaction: discord.Interaction) -> None:
        checkout_url = await self.billing_service.create_checkout_session(interaction.guild_id)
        await interaction.response.send_message(f"請至以下連結完成升級：{checkout_url}", ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BillingCog(bot))
