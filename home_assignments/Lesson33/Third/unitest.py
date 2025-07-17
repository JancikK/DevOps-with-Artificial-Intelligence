# test_main.py

import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        pass

    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    @unittest.skip("This test is skipped intentionally for demonstration")
    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    @unittest.expectedFailure
    def test_multiply(self):
        # Deliberate mistake: should be 15, but we assert wrong result
        result = self.calc.multiply(3, 5)
        self.assertEqual(result, 12)  # Incorrect on purpose

    def test_divide(self):
        result = self.calc.divide(8, 2)
        self.assertEqual(result, 4.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
