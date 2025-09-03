import unittest
from src.app import add, multiply, divide

class TestPrecision(unittest.TestCase):
    def test_inverse_mul_div(self):
        # b != 0 のとき、(a*b)/b ≒ a
        for a, b in [(7, 2), (1, 3), (-5, 8), (123456, -7)]:
            self.assertAlmostEqual(divide(multiply(a, b), b), float(a), places=12)

    def test_divide_fraction_precision(self):
        # 1/3 のような循環小数は誤差込みで近似確認
        self.assertAlmostEqual(divide(1, 3) * 3, 1.0, places=12)
