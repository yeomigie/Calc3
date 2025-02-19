from calculator import Calculator

calc = Calculator()

# Perform calculations
print(calc.perform_calculation(10, 5, "+"))  # Output: 15.0
print(calc.perform_calculation(10, 5, "-"))  # Output: 5.0
print(calc.perform_calculation(10, 5, "*"))  # Output: 50.0
print(calc.perform_calculation(10, 5, "/"))  # Output: 2.0

# Check history
for calculation in Calculator.get_history():
    print(calculation)
    from faker import Faker
fake = Faker()

def test_example():
    a = fake.random_int()
    b = fake.random_int()
    # Your test logic here
