import random

def show_title():
    print("\n" + "=" * 60)
    print("🏦 GANESH'S BANK MANAGEMENT SYSTEM 🏦")
    print("=" * 60)


def show_menu():
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

account_created = False

account_holder = ""

pin = ""

balance = 0

transactions = []

account_number = ""

while True:

    show_title()

    show_menu()

    choice = input("\nEnter Choice: ")

    if choice == "1":

        if account_created:
            print("\n❌ Account Already Exists!")

        else:

            account_holder = input("Enter Account Holder Name: ")

            while True:

                pin = input("Create 4 Digit PIN: ")

                if pin.isdigit() and len(pin) == 4:
                    break

                print("❌ PIN must contain exactly 4 digits.")

            account_number = random.randint(1000000000,9999999999)

            balance = 0

            transactions.append("Account Created")

            account_created = True

            print("\n✅ Account Created Successfully!")
            print(f"🏦 Account Number : {account_number}")

    elif choice == "2":

        if not account_created:

            print("\n❌ Please Create an Account First.")

        else:

            entered_pin = input("Enter PIN: ")

        if entered_pin == pin:

            try:

                amount = float(input("Enter Deposit Amount: "))

                if amount <= 0:

                    print("❌ Amount must be greater than zero.")

                else:

                    balance += amount

                    transactions.append(f"Deposited ₹{amount}")

                    print("\n✅ Amount Deposited Successfully!")

            except ValueError:

                print("❌ Invalid Amount.")

        else:

                print("\n❌ Incorrect PIN.")

    elif choice == "3":

        if not account_created:

            print("\n❌ Please Create an Account First.")

        else:

            entered_pin = input("Enter PIN: ")

            if entered_pin == pin:

                amount = float(input("Enter Withdrawal Amount: "))

                if amount <= balance:

                    balance -= amount

                    transactions.append(f"Withdraw ₹{amount}")

                    print("\n✅ Withdrawal Successful!")

                else:

                    print("\n❌ Insufficient Balance.")

            else:

                print("\n❌ Incorrect PIN.")
    elif choice == "4":

        if not account_created:

            print("\n❌ Please Create an Account First.")

        else:

            entered_pin = input("Enter PIN: ")

            if entered_pin == pin:

                print(f"\n💰 Current Balance : ₹{balance}")

            else:

                print("\n❌ Incorrect PIN.")

    elif choice == "5":

        if not account_created:

            print("\n❌ Please Create an Account First.")

        else:

            print("\n📜 Transaction History")

            print("-" * 40)

            for transaction in transactions:

                print(transaction)
    elif choice == "6":

        print("\n👋 Thank You For Using Bank Management System!")

        break
    else:

        print("\n❌ Invalid Choice!")

    input("\nPress Enter to Continue...")
        