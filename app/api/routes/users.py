"""Admin endpoints for inspecting users."""
from fastapi import APIRouter

from app.api.schemas.user_schema import UserOut
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.get("/{discord_id}", response_model=UserOut)
async def get_user(discord_id: int) -> UserOut:
    user = await user_service.get_or_create(discord_id)
    return UserOut.model_validate(user)
