import unittest
from src.app import divide

class TestDivide(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(divide(6, 3), 2)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(1, 0)
