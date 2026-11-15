"""Build quote receipts from shared pricing, currency and service metadata."""
from config import CURRENCY
from health import service_label
from pricing import total_cents


def build_receipt(items):
    return {
        "total_cents": total_cents(items),
        "currency": CURRENCY,
        "label": service_label(),
    }
