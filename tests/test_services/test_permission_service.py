"""Unit tests for plan-tier permission checks."""
from app.services.permission_service import PLAN_ORDER


def test_plan_order_is_ranked_low_to_high():
    assert PLAN_ORDER.index("free") < PLAN_ORDER.index("pro") < PLAN_ORDER.index("enterprise")
