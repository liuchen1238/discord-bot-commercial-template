"""Data access for the User model."""
from sqlalchemy import select

from app.database.session import get_session
from app.models.user import User


class UserRepository:
    async def get_or_create(self, discord_id: int) -> User:
        async with get_session() as session:
            result = await session.execute(select(User).where(User.discord_id == discord_id))
            user = result.scalar_one_or_none()
            if user is None:
                user = User(discord_id=discord_id)
                session.add(user)
                await session.commit()
                await session.refresh(user)
            return user
