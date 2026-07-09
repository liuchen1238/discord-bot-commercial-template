"""Inbound webhook endpoints (Stripe events)."""
from fastapi import APIRouter, Header, HTTPException, Request

from app.core.config import get_settings
from app.integrations.stripe import construct_webhook_event
from app.services.subscription_service import SubscriptionService

router = APIRouter()
settings = get_settings()
subscription_service = SubscriptionService()


@router.post("/stripe")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)) -> dict:
    payload = await request.body()
    try:
        event = construct_webhook_event(payload, stripe_signature)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Invalid webhook payload") from exc

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        guild_id = int(session["client_reference_id"])
        await subscription_service.activate(guild_id, "pro", session["subscription"])
    elif event["type"] == "customer.subscription.deleted":
        session = event["data"]["object"]
        guild_id = int(session["metadata"].get("guild_id", 0))
        await subscription_service.cancel(guild_id)

    return {"received": True}
