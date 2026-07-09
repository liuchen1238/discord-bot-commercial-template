"""Logs every mutating API request to the audit trail."""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.services.audit_service import AuditService


class AuditMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.audit_service = AuditService()

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        if request.method in ("POST", "PUT", "PATCH", "DELETE"):
            await self.audit_service.record(actor_id=0, action=f"{request.method} {request.url.path}")
        return response
