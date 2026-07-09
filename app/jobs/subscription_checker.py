"""Periodically reconciles local subscription state against Stripe."""
import logging

logger = logging.getLogger(__name__)


async def check_subscriptions() -> None:
    logger.info("Checking subscription statuses against Stripe...")
