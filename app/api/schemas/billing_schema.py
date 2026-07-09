"""Pydantic schemas for billing API requests/responses."""
from pydantic import BaseModel


class CheckoutRequest(BaseModel):
    guild_id: int


class CheckoutResponse(BaseModel):
    checkout_url: str
