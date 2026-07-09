"""Business logic for end-user profiles."""
from app.database.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def get_or_create(self, discord_user_id: int):
        return await self.repository.get_or_create(discord_user_id)
