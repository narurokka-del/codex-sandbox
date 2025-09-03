import unittest
from src.app import add, multiply, divide

class TestBigNumbers(unittest.TestCase):
    def test_very_big_integers(self):
        x = 10**100
        y = 10**50
        self.assertEqual(add(x, y), x + y)
        self.assertEqual(multiply(x, y), x * y)
        # divide は float を返すので、Python の float 計算結果と一致をチェック
        self.assertEqual(divide(x, y), float(x) / y)
