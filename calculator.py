def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid operation.")
        return

    # Input two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
