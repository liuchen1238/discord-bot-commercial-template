"""Endpoints for creating checkout/portal sessions from a dashboard front-end."""
from fastapi import APIRouter

from app.api.schemas.billing_schema import CheckoutRequest, CheckoutResponse
from app.services.billing_service import BillingService

router = APIRouter()
billing_service = BillingService()


@router.post("/checkout", response_model=CheckoutResponse)
async def create_checkout(request: CheckoutRequest) -> CheckoutResponse:
    url = await billing_service.create_checkout_session(request.guild_id)
    return CheckoutResponse(checkout_url=url)
