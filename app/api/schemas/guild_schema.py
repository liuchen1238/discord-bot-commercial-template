"""Pydantic schemas for guild API responses."""
from pydantic import BaseModel, ConfigDict


class GuildOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    active: bool
