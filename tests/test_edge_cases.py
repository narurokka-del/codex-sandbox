import unittest
from src.app import add, multiply, divide

class TestEdgeCases(unittest.TestCase):
    def test_divide_returns_float(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 123456789), 0)
        self.assertEqual(multiply(987, 0), 0)

    def test_add_negative(self):
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(-5, -3), -8)

    def test_multiply_commutative(self):
        for a, b in [(2, 3), (-4, 5), (0, 7), (-6, -8)]:
            self.assertEqual(multiply(a, b), multiply(b, a))

    def test_divide_raises_zero(self):
        with self.assertRaisesRegex(ValueError, "division by zero"):
            divide(10, 0)
