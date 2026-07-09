"""Admin endpoints for inspecting/managing registered guilds."""
from fastapi import APIRouter, HTTPException

from app.api.schemas.guild_schema import GuildOut
from app.services.guild_service import GuildService

router = APIRouter()
guild_service = GuildService()


@router.get("/{guild_id}", response_model=GuildOut)
async def get_guild(guild_id: int) -> GuildOut:
    guild = await guild_service.repository.get(guild_id)
    if guild is None:
        raise HTTPException(status_code=404, detail="Guild not found")
    return GuildOut.model_validate(guild)
