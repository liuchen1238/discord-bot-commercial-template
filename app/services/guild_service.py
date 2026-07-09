"""Business logic for guild registration and settings."""
from app.database.repositories.guild_repository import GuildRepository


class GuildService:
    def __init__(self):
        self.repository = GuildRepository()

    async def register_guild(self, guild_id: int, name: str, owner_id: int):
        return await self.repository.get_or_create(guild_id, name, owner_id)

    async def deactivate_guild(self, guild_id: int) -> None:
        await self.repository.set_active(guild_id, active=False)

    async def get_settings(self, guild_id: int) -> dict:
        guild = await self.repository.get(guild_id)
        return guild.settings if guild else {}
