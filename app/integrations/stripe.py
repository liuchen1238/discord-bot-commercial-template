"""Stripe checkout/portal/webhook helpers."""
import stripe

from app.core.config import get_settings

settings = get_settings()
stripe.api_key = settings.stripe_api_key


async def create_checkout_session(guild_id: int):
    return stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": settings.stripe_price_id_pro, "quantity": 1}],
        success_url="https://example.com/billing/success",
        cancel_url="https://example.com/billing/cancel",
        client_reference_id=str(guild_id),
    )


async def create_portal_session(customer_id: str):
    return stripe.billing_portal.Session.create(
        customer=customer_id,
        return_url="https://example.com/billing",
    )


def construct_webhook_event(payload: bytes, signature: str):
    return stripe.Webhook.construct_event(payload, signature, settings.stripe_webhook_secret)
