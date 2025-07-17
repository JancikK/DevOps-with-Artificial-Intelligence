# test_main_pytest.py

import pytest
from main import Calculator  # Import the Calculator class from your main program

# This fixture creates a new Calculator object before each test
@pytest.fixture
def calc():
    return Calculator()

# Test the add function
def test_add(calc):
    result = calc.add(2, 3)
    print(f"Test Add: 2 + 3 = {result}")
    assert result == 5  # Expected result: 5

# Test the subtract function
def test_subtract(calc):
    result = calc.subtract(10, 4)
    print(f"Test Subtract: 10 - 4 = {result}")
    assert result == 6  # Expected result: 6

# Test the multiply function
def test_multiply(calc):
    result = calc.multiply(3, 5)
    print(f"Test Multiply: 3 * 5 = {result}")
    assert result == 15  # Expected result: 15

# Test the divide function
def test_divide(calc):
    result = calc.divide(8, 2)
    print(f"Test Divide: 8 / 2 = {result}")
    assert result == 4.0  # Expected result: 4.0

# Test dividing by zero, which should raise a ValueError
def test_divide_by_zero(calc):
    print("Test Divide by Zero: 10 / 0 (Expecting ValueError)")
    with pytest.raises(ValueError):
        calc.divide(10, 0)
