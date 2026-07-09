"""Creates all tables directly (dev convenience; use Alembic migrations in production)."""
import asyncio

from app.database.base import Base
from app.database.session import engine
from app.models import audit_log, feature_flag, guild, plan, subscription, user  # noqa: F401


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created.")


if __name__ == "__main__":
    asyncio.run(main())
