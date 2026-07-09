"""Simple in-memory rate limiting middleware for the admin API."""
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

WINDOW_SECONDS = 60
MAX_REQUESTS = 120


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self._hits: dict[str, list[float]] = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        now = time.monotonic()
        hits = [t for t in self._hits.get(client_ip, []) if now - t < WINDOW_SECONDS]

        if len(hits) >= MAX_REQUESTS:
            return JSONResponse({"detail": "Too many requests"}, status_code=429)

        hits.append(now)
        self._hits[client_ip] = hits
        return await call_next(request)
