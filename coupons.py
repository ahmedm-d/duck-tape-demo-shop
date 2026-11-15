"""Coupon policy for the intentionally imperfect public demo fixture."""
from config import WELCOME_DISCOUNT_PERCENT


def apply_coupon(subtotal_cents: int, coupon: str | None = None) -> int:
    if coupon is None:
        return subtotal_cents
    if coupon != "WELCOME10":
        raise ValueError("unknown coupon")
    return max(0, subtotal_cents - WELCOME_DISCOUNT_PERCENT)
