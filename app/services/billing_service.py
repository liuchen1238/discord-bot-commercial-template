"""Wraps Stripe checkout/portal session creation for guild subscriptions."""
from app.integrations.stripe import create_checkout_session, create_portal_session


class BillingService:
    async def create_checkout_session(self, guild_id: int) -> str:
        session = await create_checkout_session(guild_id)
        return session.url

    async def create_portal_session(self, customer_id: str) -> str:
        session = await create_portal_session(customer_id)
        return session.url
