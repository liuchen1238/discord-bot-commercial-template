"""Data access for the AuditLog model."""
from app.database.session import get_session
from app.models.audit_log import AuditLog


class AuditRepository:
    async def create(self, actor_id: int, action: str, target: str | None, metadata: dict) -> AuditLog:
        async with get_session() as session:
            log = AuditLog(actor_discord_id=actor_id, action=action, target=target, metadata_=metadata)
            session.add(log)
            await session.commit()
            await session.refresh(log)
            return log
