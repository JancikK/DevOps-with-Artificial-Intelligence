# test_main.py

import unittest
from main import Calculator  # Make sure this matches your file name

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This runs before each test — used to prepare objects
        self.calc = Calculator()

    def tearDown(self):
        # This runs after each test — useful for cleanup (not used here)
        pass

    def test_add(self):
        result = self.calc.add(2, 3)
        print(f"Test Add: 2 + 3 = {result}")
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        print(f"Test Subtract: 10 - 4 = {result}")
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calc.multiply(3, 5)
        print(f"Test Multiply: 3 * 5 = {result}")
        self.assertEqual(result, 15)

    def test_divide(self):
        result = self.calc.divide(8, 2)
        print(f"Test Divide: 8 / 2 = {result}")
        self.assertEqual(result, 4.0)

    def test_divide_by_zero(self):
        print("Test Divide by Zero: 10 / 0 (Expect Error)")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# Run all tests when this file is executed
if __name__ == '__main__':
    unittest.main()
