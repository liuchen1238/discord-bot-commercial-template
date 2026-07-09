"""User-facing commands (profile, preferences, usage stats)."""
import discord
from discord.ext import commands

from app.services.user_service import UserService


class UserCog(commands.Cog, name="User"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.user_service = UserService()

    @commands.hybrid_command(name="profile", description="查看你的個人資料")
    async def profile(self, ctx: commands.Context) -> None:
        profile = await self.user_service.get_or_create(ctx.author.id)
        embed = discord.Embed(title=f"{ctx.author.display_name} 的資料")
        embed.add_field(name="加入時間", value=str(profile.created_at))
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserCog(bot))
