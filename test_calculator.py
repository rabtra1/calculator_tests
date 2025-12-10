import unittest
from main import add, sub, mul, div

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertAlmostEqual(add(0.5, 0.3), 0.8)

    def test_sub(self):
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(0, 100), 0)
        self.assertEqual(mul(-3, 3), -9)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(1, 3), 1/3)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


if __name__ == '__main__':
    unittest.main()
