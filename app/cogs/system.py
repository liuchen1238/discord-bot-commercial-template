"""Health / diagnostics commands (latency, uptime, version)."""
import time

from discord.ext import commands

START_TIME = time.monotonic()


class SystemCog(commands.Cog, name="System"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="ping", description="查看 Bot 延遲")
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send(f"Pong! `{round(self.bot.latency * 1000)}ms`")

    @commands.hybrid_command(name="uptime", description="查看 Bot 運行時間")
    async def uptime(self, ctx: commands.Context) -> None:
        seconds = int(time.monotonic() - START_TIME)
        await ctx.send(f"已運行 {seconds // 3600} 小時 {(seconds % 3600) // 60} 分鐘")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SystemCog(bot))
