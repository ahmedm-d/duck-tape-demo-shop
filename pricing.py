"""An intentionally incorrect helper for Duck Tape's public integration demo."""
from config import TAX_BASIS_POINTS


def subtotal_cents(items):
    # Intentional demo bug: quantity is ignored across the endpoint/helper boundary.
    return sum(item["price_cents"] for item in items)


def total_cents(items):
    subtotal = subtotal_cents(items)
    return subtotal + subtotal * TAX_BASIS_POINTS // 10000
