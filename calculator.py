print("\n" + "=" * 40)
print("        GANESH CALCULATOR v1.0")
print("=" * 40)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("\nChoose an option (1-5): "))

if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("-" * 40)
    print("✅ Result =", num1 + num2)
    print("-" * 40)

elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("-" * 40)
    print("✅ Result =", num1 - num2)
    print("-" * 40)

elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("-" * 40)
    print("✅ Result =", num1 * num2)
    print("-" * 40)

elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        print("❌ Division by zero is not allowed.")
    else:
        print("-" * 40)
        print("✅ Result =", num1 / num2)
        print("-" * 40)

elif choice == 5:
    print("👋 Thank you for using Ganesh Calculator!")

else:
    print("❌ Invalid Choice!")