import unittest

from app import quote_handler


class CouponSmokeTests(unittest.TestCase):
    def test_welcome_coupon_on_one_euro(self):
        result = quote_handler({"items": [{"price_cents": 100, "quantity": 1}], "coupon": "WELCOME10"})
        self.assertEqual(result["total_cents"], 99)
        self.assertEqual(result["currency"], "EUR")

    def test_unknown_coupon_is_rejected(self):
        with self.assertRaises(ValueError):
            quote_handler({"items": [], "coupon": "UNKNOWN"})

    def test_non_text_coupon_is_rejected(self):
        with self.assertRaises(ValueError):
            quote_handler({"items": [], "coupon": 10})
