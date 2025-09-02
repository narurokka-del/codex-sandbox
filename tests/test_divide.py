import unittest
from src.app import divide

class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
