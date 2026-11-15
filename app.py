"""Loopback-only demo endpoint: POST /quote with {items: [...]} JSON."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from config import CURRENCY
from legacy import legacy_label
from pricing import total_cents


def quote_handler(payload):
    items = payload.get("items", [])
    if not isinstance(items, list) or len(items) > 100:
        raise ValueError("items must be a list with at most 100 entries")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("each item must be an object")
        for field in ("price_cents", "quantity"):
            value = item.get(field)
            if type(value) is not int or not 0 <= value <= 1000000:
                raise ValueError(field + " must be a bounded non-negative integer")
    return {"total_cents": total_cents(items), "currency": CURRENCY, "label": legacy_label()}


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/quote":
            self.send_error(404)
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 1 <= size <= 16384:
                raise ValueError("invalid body size")
            payload = json.loads(self.rfile.read(size))
            if not isinstance(payload, dict):
                raise ValueError("body must be an object")
            body = json.dumps(quote_handler(payload)).encode()
        except (ValueError, TypeError):
            self.send_error(400, "Invalid quote request")
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8899), Handler).serve_forever()
