"""Daily cleanup of stale data (expired tokens, inactive guild records, etc.)."""
import logging

logger = logging.getLogger(__name__)


async def run_cleanup() -> None:
    logger.info("Running daily cleanup job...")
