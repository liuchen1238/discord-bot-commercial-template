"""Entry point for running the Discord bot process."""
import asyncio

from app.bot import build_bot
from app.core.config import get_settings
from app.core.logging import setup_logging


async def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)

    bot = build_bot(settings)
    async with bot:
        await bot.start(settings.discord_token)


if __name__ == "__main__":
    asyncio.run(main())
