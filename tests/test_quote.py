import unittest

from app import quote_handler
from config import CURRENCY


class QuoteTests(unittest.TestCase):
    def test_single_item(self):
        result = quote_handler({"items": [{"price_cents": 100, "quantity": 1}]})
        self.assertEqual(result["total_cents"], 110)
        self.assertEqual(result["currency"], CURRENCY)

    def test_quantity_regression(self):
        # Preserve the earlier quantity repair across endpoint/helper/config.
        result = quote_handler({"items": [{"price_cents": 100, "quantity": 2}]})
        self.assertEqual(result["total_cents"], 220)

    def test_quantity_multiple_items(self):
        # Regression test: quantity must be multiplied before tax.
        # Two items: 100 cents × qty 3 + 200 cents × qty 2 = 700 subtotal, 770 with 10% tax
        result = quote_handler({
            "items": [
                {"price_cents": 100, "quantity": 3},
                {"price_cents": 200, "quantity": 2}
            ]
        })
        self.assertEqual(result["total_cents"], 770)
        self.assertEqual(result["currency"], CURRENCY)

    def test_empty(self):
        self.assertEqual(quote_handler({"items": []})["total_cents"], 0)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            quote_handler({"items": [{"price_cents": 100, "quantity": -1}]})
