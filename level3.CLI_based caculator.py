def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


def get_numbers():
    while True:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def show_menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculator():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Try again.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print(f"Result: {result}")


if __name__ == "__main__":
    calculator()
