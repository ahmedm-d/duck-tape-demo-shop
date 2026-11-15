import unittest

from app import quote_handler
from config import CURRENCY


class QuoteTests(unittest.TestCase):
    def test_single_item(self):
        result = quote_handler({"items": [{"price_cents": 100, "quantity": 1}]})
        self.assertEqual(result["total_cents"], 110)
        self.assertEqual(result["currency"], CURRENCY)

    def test_quantity_regression(self):
        # Deliberately fails: endpoint -> pricing helper -> configured tax.
        result = quote_handler({"items": [{"price_cents": 100, "quantity": 2}]})
        self.assertEqual(result["total_cents"], 220)

    def test_empty(self):
        self.assertEqual(quote_handler({"items": []})["total_cents"], 0)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            quote_handler({"items": [{"price_cents": 100, "quantity": -1}]})
