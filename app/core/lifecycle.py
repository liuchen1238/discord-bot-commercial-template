"""Startup / shutdown hooks shared by the bot process and the API process."""
import logging

from app.database.session import engine
from app.jobs.scheduler import start_scheduler, stop_scheduler

logger = logging.getLogger(__name__)


async def on_startup() -> None:
    logger.info("Starting up...")
    start_scheduler()


async def on_shutdown() -> None:
    logger.info("Shutting down...")
    stop_scheduler()
    await engine.dispose()
