def show_menu():
    print("\n" + "=" * 45)
    print("          🧮 GANESH CALCULATOR")
    print("=" * 45)
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    print("5. % Modulus")
    print("6. ^ Power")
    print("7. 🚪 Exit")
    print("=" * 45)


while True:
    show_menu()

    try:
        choice = int(input("Choose an option (1-7): "))

        if choice == 7:
            print("\n👋 Thank you for using Ganesh Calculator!")
            print("Have a great day ❤️")
            break

        if choice not in [1, 2, 3, 4, 5, 6]:
            print("❌ Invalid choice!")
            continue

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
            operation = "+"

        elif choice == 2:
            result = num1 - num2
            operation = "-"

        elif choice == 3:
            result = num1 * num2
            operation = "*"

        elif choice == 4:
            if num2 == 0:
                print("❌ Division by zero is not allowed.")
                continue
            result = num1 / num2
            operation = "/"

        elif choice == 5:
            result = num1 % num2
            operation = "%"

        elif choice == 6:
            result = num1 ** num2
            operation = "^"

        print("\n" + "-" * 45)
        print(f"Result : {num1} {operation} {num2} = {result}")
        print("-" * 45)

    except ValueError:
        print("❌ Please enter valid numbers only.")