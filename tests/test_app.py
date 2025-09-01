import unittest
from src.app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
def test_add_negative(self):
    self.assertEqual(add(-2, 3), 1)

def test_add_zero(self):
    self.assertEqual(add(0, 5), 5)
