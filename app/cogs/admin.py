"""Owner-only commands for bot administration across all guilds."""
from discord.ext import commands

from app.services.audit_service import AuditService


class AdminCog(commands.Cog, name="Admin"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.audit_service = AuditService()

    @commands.is_owner()
    @commands.command(name="sync")
    async def sync_commands(self, ctx: commands.Context) -> None:
        synced = await self.bot.tree.sync()
        await ctx.send(f"已同步 {len(synced)} 個指令。")

    @commands.is_owner()
    @commands.command(name="maintenance")
    async def toggle_maintenance(self, ctx: commands.Context, state: bool) -> None:
        self.bot.settings.maintenance_mode = state
        await ctx.send(f"維護模式：{'開啟' if state else '關閉'}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AdminCog(bot))
