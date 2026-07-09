"""Thin wrapper around discord.py REST helpers used outside the bot process (e.g. from the API)."""
import discord


async def fetch_guild_icon_url(guild_id: int, bot: discord.Client) -> str | None:
    guild = bot.get_guild(guild_id)
    return guild.icon.url if guild and guild.icon else None
