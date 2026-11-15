"""Quote totals in integer cents; coupons are applied before tax."""
from config import TAX_BASIS_POINTS
from coupons import apply_coupon


def subtotal_cents(items):
    return sum(item["price_cents"] * item["quantity"] for item in items)


def total_cents(items, coupon=None):
    subtotal = apply_coupon(subtotal_cents(items), coupon)
    return subtotal + subtotal * TAX_BASIS_POINTS // 10000
