"""Standalone script to sync slash commands without starting the full bot loop."""
import asyncio

from app.bot import build_bot
from app.core.config import get_settings


async def main() -> None:
    settings = get_settings()
    bot = build_bot(settings)

    @bot.event
    async def on_ready():
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")
        await bot.close()

    await bot.start(settings.discord_token)


if __name__ == "__main__":
    asyncio.run(main())
