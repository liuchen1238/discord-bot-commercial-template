"""Records administrative and billing actions for later auditing."""
from app.database.repositories.audit_repository import AuditRepository


class AuditService:
    def __init__(self):
        self.repository = AuditRepository()

    async def record(self, actor_id: int, action: str, target: str | None = None, metadata: dict | None = None):
        await self.repository.create(actor_id, action, target, metadata or {})
