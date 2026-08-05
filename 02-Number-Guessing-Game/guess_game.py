import random
import time


def show_title():
    print("\n" + "=" * 50)
    print("🎮 GANESH'S GUESSING GAME")
    print("=" * 50)
    print("🌟 Challenge yourself and beat your Best Score!")
    print("=" * 50)


best_score = None

while True:

    show_title()

    print("Loading Game", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    print("🟢 1. Easy (1-50)")
    print("🟡 2. Medium (1-100)")
    print("🟠 3. Hard (1-500)")
    print("🔴 4. Impossible (1-1000)")

    try:
        difficulty = int(input("\nChoose Difficulty (1-4): "))
    except ValueError:
        print("\n❌ Please enter only numbers.\n")
        continue

    if difficulty == 1:
        max_number = 50
        print("\n🟢 Easy Mode Selected")
        print("🎯 Guess a number between 1 and 50\n")

    elif difficulty == 2:
        max_number = 100
        print("\n🟡 Medium Mode Selected")
        print("🎯 Guess a number between 1 and 100\n")

    elif difficulty == 3:
        max_number = 500
        print("\n🟠 Hard Mode Selected")
        print("🎯 Guess a number between 1 and 500\n")

    elif difficulty == 4:
        max_number = 1000
        print("\n🔴 Impossible Mode Selected 😈")
        print("🎯 Guess a number between 1 and 1000\n")

    else:
        print("\n❌ Invalid Choice!\n")
        continue

    secret_number = random.randint(1, max_number)

    attempts = 0

    while True:

        try:
            guess = int(input(f"Guess the number (1-{max_number}): "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too Low!\n")

        elif guess > secret_number:
            print("📈 Too High!\n")

        else:
            print("\n" + "=" * 50)
            print("🎉 GAME COMPLETED 🎉")
            print("=" * 50)
            print(f"🥳 Correct Number : {secret_number}")
            print(f"📊 Attempts       : {attempts}")

            if best_score is None or attempts < best_score:
                best_score = attempts
                print("🏆 New Best Score!")
            else:
                print("👏 Try again to beat your Best Score!")

            print(f"⭐ Best Score     : {best_score}")
            print("=" * 50)
            print("❤️ Thanks for playing Ganesh's Guessing Game!")
            print("=" * 50)
            break

    while True:

        play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()

        if play_again == "y":
            print("\n🔄 Restarting Game...")
            time.sleep(1)
            break

        elif play_again == "n":
            print("\n👋 Thank you for playing!")
            print("❤️ See you again, Ganesh!")
            exit()

        else:
            print("❌ Please enter only 'y' or 'n'.")