import random
import string


def show_title():
    print("\n" + "=" * 60)
    print("🔐 GANESH'S PASSWORD GENERATOR 🔐")
    print("=" * 60)


def get_yes_no(message):
    while True:
        choice = input(message).lower()

        if choice in ["y", "n"]:
            return choice

        print("❌ Please enter only y or n.")


def generate_password(length, use_upper, use_numbers, use_symbols):

    characters = string.ascii_lowercase
    password = []

    # Always include one lowercase letter
    password.append(random.choice(string.ascii_lowercase))

    if use_upper == "y":
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if use_numbers == "y":
        characters += string.digits
        password.append(random.choice(string.digits))

    if use_symbols == "y":
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    remaining = length - len(password)

    for _ in range(remaining):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


def password_strength(length, upper, numbers, symbols):

    score = 0

    if length >= 8:
        score += 1

    if length >= 12:
        score += 1

    if upper == "y":
        score += 1

    if numbers == "y":
        score += 1

    if symbols == "y":
        score += 1

    if score <= 2:
        return "🔴 Weak"

    elif score <= 4:
        return "🟡 Medium"

    return "🟢 Strong"


while True:

    show_title()

    while True:

        try:

            length = int(input("Enter Password Length: "))

            if length < 4:
                print("❌ Password length must be at least 4.")

            else:
                break

        except ValueError:
            print("❌ Please enter a valid number.")

    use_upper = get_yes_no("Include Uppercase Letters? (y/n): ")
    use_numbers = get_yes_no("Include Numbers? (y/n): ")
    use_symbols = get_yes_no("Include Symbols? (y/n): ")

    password = generate_password(
        length,
        use_upper,
        use_numbers,
        use_symbols
    )

    strength = password_strength(
        length,
        use_upper,
        use_numbers,
        use_symbols
    )

    print("\n" + "=" * 60)
    print("🔑 GENERATED PASSWORD")
    print("=" * 60)
    print(password)
    print("=" * 60)

    print(f"📊 Password Strength : {strength}")

    print("\nCharacter Set Used")
    print("----------------------------")
    print("✅ Lowercase : Yes")
    print(f"✅ Uppercase : {'Yes' if use_upper == 'y' else 'No'}")
    print(f"✅ Numbers   : {'Yes' if use_numbers == 'y' else 'No'}")
    print(f"✅ Symbols   : {'Yes' if use_symbols == 'y' else 'No'}")

    print("=" * 60)
    
    again = get_yes_no("\nGenerate Another Password? (y/n): ")

    if again == "n":
        print("\n👋 Thank you for using Ganesh's Password Generator!")
        print("❤️ See you again!")
        break