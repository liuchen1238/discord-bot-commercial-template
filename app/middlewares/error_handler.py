"""Converts unhandled application exceptions into consistent JSON error responses."""
import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.exceptions import AppError

logger = logging.getLogger(__name__)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except AppError as exc:
            logger.warning("Application error: %s", exc)
            return JSONResponse({"detail": str(exc)}, status_code=400)
        except Exception:
            logger.exception("Unhandled error")
            return JSONResponse({"detail": "Internal server error"}, status_code=500)
