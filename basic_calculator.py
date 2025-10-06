# basic_calculator.py
# A simple calculator that performs basic arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Cannot divide by zero!" if y == 0 else x / y

if __name__ == "__main__":
    print("🧮 Simple Python Calculator 🧮")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")
