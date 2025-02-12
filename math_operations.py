from typing import List
from datetime import datetime

class MathOperations:
    """A calculator that performs basic arithmetic operations and stores history with timestamps."""

    _history: List[dict] = []

    def __init__(self):
        """Initialize the calculator with a welcome message."""
        print("Welcome to the Math Operations Calculator!")

    @staticmethod
    def add_numbers(a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract_numbers(a: float, b: float) -> float:
        """Returns the difference of two numbers."""
        return a - b

    @staticmethod
    def multiply_numbers(a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide_numbers(a: float, b: float) -> float:
        """Returns the quotient of two numbers. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @classmethod
    def add_to_history(cls, operation: str, a: float, b: float, result: float) -> None:
        """Adds a calculation to the history with a timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cls._history.append({
            "timestamp": timestamp,
            "operation": operation,
            "operand1": a,
            "operand2": b,
            "result": result,
        })

    @classmethod
    def show_history(cls) -> None:
        """Displays the calculation history in a formatted way."""
        if not cls._history:
            print("No calculations in history.")
            return

        print("\nCalculation History:")
        for entry in cls._history:
            print(
                f"{entry['timestamp']}: "
                f"{entry['operand1']} {entry['operation']} {entry['operand2']} = {entry['result']}"
            )

    def perform_operation(self, a: float, b: float, operation: str) -> float:
        """Performs a calculation and stores it in history."""
        operations = {
            "+": self.add_numbers,
            "-": self.subtract_numbers,
            "*": self.multiply_numbers,
            "/": self.divide_numbers,
        }

        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")

        try:
            result = operations[operation](a, b)
            self.add_to_history(operation, a, b, result)
            return result
        except Exception as e:
            raise e
