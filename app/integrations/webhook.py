"""Generic outbound webhook sender (used for developer/admin notifications)."""
import httpx

from app.core.config import get_settings

settings = get_settings()


async def send_webhook_message(content: str, webhook_url: str | None = None) -> None:
    url = webhook_url or getattr(settings, "notification_webhook_url", "")
    if not url:
        return
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"content": content})
