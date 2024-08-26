# Python Programming Assignment 05
import random

if __name__ == '__main__':
    rounds: int = 5
    user_score: int = 0
    computer_score: int = 0

    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for i in range(1, rounds + 1):
        user_rand_num: int = random.randint(1, 100)
        computer_rand_num: int = random.randint(1, 100)
        print(f"\nRound {i}:")
        print(f"Your number is {user_rand_num}")

        high_or_low: str = input("Do you think your number is higher or lower than the computer's?: ")
        if high_or_low == "higher":
            if user_rand_num > computer_rand_num:
                print(f"You were right! The computer's number was {computer_rand_num}")
                user_score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_rand_num}")
                computer_score += 1
        else:
            if user_rand_num < computer_rand_num:
                print(f"You were right! The computer's number was {computer_rand_num}")
                user_score += 1
            else:
                print(f"Aww, that's incorrect. The computer's number was {computer_rand_num}")
                computer_score += 1

        print(f"Your score is now {user_score}")

    print("\nThanks for playing!")

