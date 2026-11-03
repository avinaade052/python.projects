def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def calculator():
    try:
        operation = input("Choose operation (+, -, *, /): ").strip()
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
