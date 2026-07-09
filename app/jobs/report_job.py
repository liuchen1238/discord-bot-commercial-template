"""Weekly usage/billing report generation."""
import logging

logger = logging.getLogger(__name__)


async def run_report() -> None:
    logger.info("Generating weekly report...")
