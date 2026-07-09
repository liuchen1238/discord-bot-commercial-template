"""Returns 503 for all non-health requests while maintenance mode is enabled."""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.config import get_settings


class MaintenanceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        settings = get_settings()
        if settings.maintenance_mode and request.url.path != "/health":
            return JSONResponse({"detail": "Service under maintenance"}, status_code=503)
        return await call_next(request)
