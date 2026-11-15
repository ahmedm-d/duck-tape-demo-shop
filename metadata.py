"""Shared receipt metadata, linked to configuration and service identity."""
from config import CURRENCY
from health import service_label


def receipt_metadata():
    return {"currency": CURRENCY, "label": service_label()}
