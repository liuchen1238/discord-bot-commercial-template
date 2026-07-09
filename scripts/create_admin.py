"""CLI helper to grant a Discord user bot-owner/admin privileges."""
import argparse
import asyncio

from app.database.repositories.user_repository import UserRepository


async def main(discord_id: int) -> None:
    repository = UserRepository()
    user = await repository.get_or_create(discord_id)
    print(f"Ensured admin user exists: {user.discord_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create/ensure an admin user record")
    parser.add_argument("discord_id", type=int)
    args = parser.parse_args()
    asyncio.run(main(args.discord_id))
