"""Data access for the Guild model."""
from app.database.session import get_session
from app.models.guild import Guild


class GuildRepository:
    async def get(self, guild_id: int) -> Guild | None:
        async with get_session() as session:
            return await session.get(Guild, guild_id)

    async def get_or_create(self, guild_id: int, name: str, owner_id: int) -> Guild:
        async with get_session() as session:
            guild = await session.get(Guild, guild_id)
            if guild is None:
                guild = Guild(id=guild_id, name=name, owner_discord_id=owner_id)
                session.add(guild)
                await session.commit()
                await session.refresh(guild)
            return guild

    async def set_active(self, guild_id: int, active: bool) -> None:
        async with get_session() as session:
            guild = await session.get(Guild, guild_id)
            if guild:
                guild.active = active
                await session.commit()
