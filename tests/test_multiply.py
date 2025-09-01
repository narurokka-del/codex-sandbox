import unittest
from src.app import multiply

class TestMultiply(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(multiply(2, 3), 6)
