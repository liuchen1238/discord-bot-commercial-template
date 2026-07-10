"""FastAPI application exposing admin/billing endpoints alongside the bot."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import billing, guilds, health, users, webhooks
from app.core.config import get_settings
from app.core.lifecycle import on_shutdown, on_startup
from app.middlewares.error_handler import ErrorHandlerMiddleware
from app.middlewares.maintenance import MaintenanceMiddleware
from app.middlewares.rate_limit import RateLimitMiddleware

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_startup()
    yield
    await on_shutdown()


app = FastAPI(title="Discord Bot Commercial Template API", version="0.1.0", lifespan=lifespan)

app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(MaintenanceMiddleware)
app.add_middleware(RateLimitMiddleware)

app.include_router(health.router, tags=["health"])
app.include_router(guilds.router, prefix="/guilds", tags=["guilds"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(billing.router, prefix="/billing", tags=["billing"])
app.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
