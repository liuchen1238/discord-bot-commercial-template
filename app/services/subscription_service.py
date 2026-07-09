"""Business logic for reading/updating a guild's subscription state."""
from app.database.repositories.subscription_repository import SubscriptionRepository


class SubscriptionService:
    def __init__(self):
        self.repository = SubscriptionRepository()

    async def get_for_guild(self, guild_id: int):
        return await self.repository.get_for_guild(guild_id)

    async def activate(self, guild_id: int, plan_slug: str, stripe_subscription_id: str):
        return await self.repository.upsert(guild_id, plan_slug, stripe_subscription_id, status="active")

    async def cancel(self, guild_id: int):
        await self.repository.set_status(guild_id, status="cancelled")
