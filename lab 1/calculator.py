# Basic calculator program with repeated calculations

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
            continue

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except EOFError:
        print("\nInput ended. Goodbye!")
        break

    try:
        again = input("Would you like to do another calculation? (y/n): ").lower()
    except EOFError:
        print("\nInput ended. Goodbye!")
        break

    if again != 'y':
        print("Goodbye!")
        break
