"""Resolves whether a guild's current plan satisfies a required feature tier."""
from app.database.repositories.subscription_repository import SubscriptionRepository

PLAN_ORDER = ["free", "pro", "enterprise"]


class PermissionService:
    def __init__(self):
        self.subscription_repository = SubscriptionRepository()

    async def has_plan(self, guild_id: int, min_plan: str) -> bool:
        subscription = await self.subscription_repository.get_for_guild(guild_id)
        current_plan = subscription.plan.slug if subscription else "free"
        return PLAN_ORDER.index(current_plan) >= PLAN_ORDER.index(min_plan)
