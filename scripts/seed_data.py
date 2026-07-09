"""Seeds default billing plans (Free / Pro / Enterprise) into the database."""
import asyncio

from app.database.session import get_session
from app.models.plan import Plan

DEFAULT_PLANS = [
    {"slug": "free", "name": "Free", "price_cents": 0, "features": {"max_guilds": 1}},
    {"slug": "pro", "name": "Pro", "price_cents": 999, "features": {"max_guilds": 5, "priority_support": True}},
    {"slug": "enterprise", "name": "Enterprise", "price_cents": 4999, "features": {"max_guilds": -1}},
]


async def main() -> None:
    async with get_session() as session:
        for data in DEFAULT_PLANS:
            session.add(Plan(**data))
        await session.commit()
    print("Seeded default plans.")


if __name__ == "__main__":
    asyncio.run(main())
