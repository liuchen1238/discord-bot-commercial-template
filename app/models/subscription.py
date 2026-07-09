"""ORM model linking a guild to its active billing plan / Stripe subscription."""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    guild_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("guilds.id"), unique=True)
    plan_id: Mapped[int] = mapped_column(Integer, ForeignKey("plans.id"))
    stripe_subscription_id: Mapped[str] = mapped_column(String(100), nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="active")
    current_period_end: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    guild = relationship("Guild", back_populates="subscription")
    plan = relationship("Plan")
