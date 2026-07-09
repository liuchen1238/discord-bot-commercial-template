"""Discovers and loads plugins from app/plugins/* as Discord.py extensions."""
import importlib
import json
import logging
from pathlib import Path

from discord.ext import commands

from app.plugins.registry import PluginInfo, registry

logger = logging.getLogger(__name__)
PLUGINS_DIR = Path(__file__).parent


async def load_plugins(bot: commands.Bot) -> None:
    for manifest_path in PLUGINS_DIR.glob("*/manifest.json"):
        plugin_dir = manifest_path.parent
        manifest = json.loads(manifest_path.read_text())

        module = importlib.import_module(f"app.plugins.{plugin_dir.name}.plugin")
        await module.setup(bot)

        registry.register(PluginInfo(name=manifest["name"], version=manifest["version"]))
        logger.info("Loaded plugin: %s v%s", manifest["name"], manifest["version"])
