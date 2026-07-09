"""Commands and listeners for guild (server) lifecycle events."""
import discord
from discord.ext import commands

from app.services.guild_service import GuildService


class GuildCog(commands.Cog, name="Guild"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild_service = GuildService()

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None:
        await self.guild_service.register_guild(guild.id, guild.name, guild.owner_id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild) -> None:
        await self.guild_service.deactivate_guild(guild.id)

    @commands.hybrid_command(name="settings", description="查看伺服器設定")
    async def settings(self, ctx: commands.Context) -> None:
        settings = await self.guild_service.get_settings(ctx.guild.id)
        await ctx.send(f"```{settings}```")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuildCog(bot))
