from math_operations import MathOperations

# Create an instance of the calculator
calc = MathOperations()

# Perform calculations
print("10 + 5 =", calc.perform_operation(10, 5, "+"))  # Output: 10 + 5 = 15.0
print("10 - 5 =", calc.perform_operation(10, 5, "-"))  # Output: 10 - 5 = 5.0
print("10 * 5 =", calc.perform_operation(10, 5, "*"))  # Output: 10 * 5 = 50.0
print("10 / 5 =", calc.perform_operation(10, 5, "/"))  # Output: 10 / 5 = 2.0

# Show history
calc.show_history()
