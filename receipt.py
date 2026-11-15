"""Assemble the quote from pricing and shared receipt metadata."""
from metadata import receipt_metadata
from pricing import total_cents


def build_receipt(items, coupon=None):
    return {"total_cents": total_cents(items, coupon), **receipt_metadata()}
