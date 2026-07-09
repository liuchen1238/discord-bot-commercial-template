"""Redis-backed task queue for offloading slow work from the bot event loop."""
import json

import redis.asyncio as redis

from app.core.config import get_settings

settings = get_settings()
redis_client = redis.from_url(settings.redis_url, decode_responses=True)

QUEUE_KEY = "app:tasks"


async def enqueue(task_name: str, payload: dict) -> None:
    await redis_client.rpush(QUEUE_KEY, json.dumps({"task": task_name, "payload": payload}))


async def dequeue() -> dict | None:
    raw = await redis_client.lpop(QUEUE_KEY)
    return json.loads(raw) if raw else None
