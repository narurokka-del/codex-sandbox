import unittest
from src.app import add, multiply, divide

class TestAlgebraLaws(unittest.TestCase):
    def test_commutativity(self):
        for a in range(-10, 11):
            for b in range(-10, 11):
                self.assertEqual(add(a, b), add(b, a))
                self.assertEqual(multiply(a, b), multiply(b, a))

    def test_distributive(self):
        for a in range(-5, 6):
            for b in range(-5, 6):
                for c in range(-5, 6):
                    self.assertEqual(
                        multiply(a, b + c),
                        add(multiply(a, b), multiply(a, c))
                    )

class TestTypeErrors(unittest.TestCase):
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            add("1", 2)
        with self.assertRaises(TypeError):
            multiply(3, "x")
        with self.assertRaises(TypeError):
            divide("10", 2)
