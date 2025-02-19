import sys

def calculate(a, b, operation):
    try:
        a = int(a)
        b = int(b)
        if operation == 'add':
            return a + b
        elif operation == 'subtract':
            return a - b
        elif operation == 'multiply':
            return a * b
        elif operation == 'divide':
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b
        else:
            raise ValueError("Unknown operation")
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <a> <b> <operation>")
    else:
        a, b, operation = sys.argv[1], sys.argv[2], sys.argv[3]
        result = calculate(a, b, operation)
        print(f"The result of {a} {operation} {b} is equal to {result}")
