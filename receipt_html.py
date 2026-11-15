"""Intentionally unsafe, unmerged demo proposal for cited PR review."""


def render_receipt_note(note: str) -> str:
    return "<!doctype html><h1>Receipt note</h1><p>" + note + "</p>"
