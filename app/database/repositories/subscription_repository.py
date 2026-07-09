"""Data access for the Subscription model."""
from sqlalchemy import select

from app.database.session import get_session
from app.models.plan import Plan
from app.models.subscription import Subscription


class SubscriptionRepository:
    async def get_for_guild(self, guild_id: int) -> Subscription | None:
        async with get_session() as session:
            result = await session.execute(
                select(Subscription).where(Subscription.guild_id == guild_id)
            )
            return result.scalar_one_or_none()

    async def upsert(self, guild_id: int, plan_slug: str, stripe_subscription_id: str, status: str) -> Subscription:
        async with get_session() as session:
            plan_result = await session.execute(select(Plan).where(Plan.slug == plan_slug))
            plan = plan_result.scalar_one()

            result = await session.execute(select(Subscription).where(Subscription.guild_id == guild_id))
            subscription = result.scalar_one_or_none()
            if subscription is None:
                subscription = Subscription(guild_id=guild_id)
                session.add(subscription)

            subscription.plan_id = plan.id
            subscription.stripe_subscription_id = stripe_subscription_id
            subscription.status = status
            await session.commit()
            await session.refresh(subscription)
            return subscription

    async def set_status(self, guild_id: int, status: str) -> None:
        async with get_session() as session:
            result = await session.execute(select(Subscription).where(Subscription.guild_id == guild_id))
            subscription = result.scalar_one_or_none()
            if subscription:
                subscription.status = status
                await session.commit()
