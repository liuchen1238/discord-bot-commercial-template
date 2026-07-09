"""Background worker loop that consumes tasks pushed onto the Redis queue."""
import asyncio
import logging

from app.workers.queue import dequeue

logger = logging.getLogger(__name__)

TASK_HANDLERS: dict[str, callable] = {}


def task(name: str):
    def decorator(func):
        TASK_HANDLERS[name] = func
        return func

    return decorator


async def run_worker(poll_interval: float = 1.0) -> None:
    while True:
        job = await dequeue()
        if job is None:
            await asyncio.sleep(poll_interval)
            continue

        handler = TASK_HANDLERS.get(job["task"])
        if handler is None:
            logger.warning("No handler registered for task %s", job["task"])
            continue

        try:
            await handler(**job["payload"])
        except Exception:
            logger.exception("Task %s failed", job["task"])
