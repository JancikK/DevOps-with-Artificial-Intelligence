# calculator.py

class Calculator:
    def __init__(self):
        # Optional: prepare for future variable storage
        self.variables = {}

    def add(self, a, b):
        # Return the sum of two numbers
        return a + b

    def subtract(self, a, b):
        # Return the difference of two numbers
        return a - b

    def multiply(self, a, b):
        # Return the product of two numbers
        return a * b

    def divide(self, a, b):
        # Raise error if trying to divide by zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# === Simple User Interaction (No choice menu) ===
if __name__ == "__main__":
    # Create a Calculator object
    calc = Calculator()

    try:
        # Ask user for two numbers
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Perform all four operations
        print(f"Addition: {calc.add(a, b)}")
        print(f"Subtraction: {calc.subtract(a, b)}")
        print(f"Multiplication: {calc.multiply(a, b)}")
        print(f"Division: {calc.divide(a, b)}")

    except ValueError as e:
        # Handle errors (e.g. divide by zero or bad input)
        print("Error:", e)
