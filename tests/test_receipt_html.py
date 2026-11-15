import unittest

from receipt_html import render_receipt_note


class ReceiptPreviewTests(unittest.TestCase):
    def test_customer_note_remains_text(self):
        # Deliberately fails on this unmerged, unsafe PR; harmless markup only.
        self.assertIn("&lt;b&gt;gift&lt;/b&gt;", render_receipt_note("<b>gift</b>"))
