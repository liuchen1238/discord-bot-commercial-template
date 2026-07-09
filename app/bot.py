"""Discord bot factory: wires up intents, cogs, and lifecycle hooks."""
import logging

import discord
from discord.ext import commands

from app.core.config import Settings
from app.core.lifecycle import on_shutdown, on_startup

logger = logging.getLogger(__name__)

INITIAL_EXTENSIONS = (
    "app.cogs.admin",
    "app.cogs.billing",
    "app.cogs.guild",
    "app.cogs.user",
    "app.cogs.support",
    "app.cogs.system",
)


class CommercialBot(commands.Bot):
    def __init__(self, settings: Settings, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents, **kwargs)
        self.settings = settings

    async def setup_hook(self) -> None:
        for extension in INITIAL_EXTENSIONS:
            await self.load_extension(extension)
        await self.tree.sync()
        await on_startup()

    async def close(self) -> None:
        await on_shutdown()
        await super().close()


def build_bot(settings: Settings) -> CommercialBot:
    return CommercialBot(settings)
