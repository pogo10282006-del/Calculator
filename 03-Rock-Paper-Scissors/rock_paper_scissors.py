import random
import time


choices = ["Rock", "Paper", "Scissors"]


def show_title():
    print("\n" + "=" * 55)
    print("🎮 GANESH'S ROCK PAPER SCISSORS 🎮")
    print("=" * 55)


def show_menu():
    print("\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")


def get_user_choice():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            return "Rock"
        elif choice == "2":
            return "Paper"
        elif choice == "3":
            return "Scissors"
        else:
            print("❌ Invalid Choice! Please try again.\n")


def get_computer_choice():
    return random.choice(choices)


def decide_winner(user, computer):
    if user == computer:
        return "Draw"

    elif (
        (user == "Rock" and computer == "Scissors") or
        (user == "Paper" and computer == "Rock") or
        (user == "Scissors" and computer == "Paper")
    ):
        return "Player"

    else:
        return "Computer"


while True:

    player_score = 0
    computer_score = 0

    show_title()

    player_name = input("👤 Enter your name: ").title()

    print(f"\nWelcome, {player_name}! 👋")

    while True:
        print("\nChoose Match Type")
        print("1. Best of 3")
        print("2. Best of 5")
        print("3. Unlimited")

        match = input("\nEnter choice: ")

        if match == "1":
            target = 2
            break

        elif match == "2":
            target = 3
            break

        elif match == "3":
            target = None
            break

        else:
            print("❌ Invalid Choice!")

    round_number = 1

    while True:

        print("\n" + "-" * 55)
        print(f"🎯 Round {round_number}")
        print("-" * 55)

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\n🧑 {player_name}: {user_choice}")
        print(f"💻 Computer: {computer_choice}")

        winner = decide_winner(user_choice, computer_choice)

        if winner == "Player":
            print("\n🎉 You Win this round!")
            player_score += 1

        elif winner == "Computer":
            print("\n😢 Computer Wins this round!")
            computer_score += 1

        else:
            print("\n🤝 It's a Draw!")

        print("\n📊 SCOREBOARD")
        print(f"🧑 {player_name}: {player_score}")
        print(f"💻 Computer: {computer_score}")

        if target is not None:

            if player_score == target or computer_score == target:
                break

        else:

            again = input("\nContinue Unlimited Match? (y/n): ").lower()

            if again == "n":
                break

        round_number += 1

    print("\n" + "=" * 55)
    print("🏆 MATCH OVER")
    print("=" * 55)

    print(f"🧑 {player_name}: {player_score}")
    print(f"💻 Computer: {computer_score}")

    if player_score > computer_score:
        print(f"\n🥳 Congratulations {player_name}! You won the match!")

    elif computer_score > player_score:
        print("\n💻 Computer won the match!")

    else:
        print("\n🤝 Match Draw!")

    print("=" * 55)

    play_again = input("\n🔁 Play Again? (y/n): ").lower()

    if play_again != "y":
        print("\n👋 Thanks for playing!")
        print("❤️ See you again!")
        break

    time.sleep(1)