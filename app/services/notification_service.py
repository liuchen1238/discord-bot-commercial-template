"""Sends notifications to developers/admins (Discord webhook, email, etc.)."""
import logging

from app.integrations.webhook import send_webhook_message

logger = logging.getLogger(__name__)


class NotificationService:
    async def notify_developers(self, message: str) -> None:
        logger.info("Developer notification: %s", message)
        await send_webhook_message(message)
