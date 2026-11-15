import unittest
from metadata import receipt_metadata

class MetadataTests(unittest.TestCase):
    def test_metadata(self):
        self.assertEqual(receipt_metadata(), {"currency": "EUR", "label": "demo quote v2"})
