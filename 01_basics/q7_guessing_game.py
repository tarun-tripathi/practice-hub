# Q7: Number Guessing Game
# Task: Build a guessing game with 3 difficulty levels
# Easy: 1-50, 10 tries | Medium: 1-100, 7 tries | Hard: 1-200, 5 tries
# Extra: Track score across rounds

import random

def play_game(difficulty):
    levels = {
        "easy": (1, 50, 10),
        "medium": (1, 100, 7),
        "hard": (1, 200, 5)
    }

    low, high, tries = levels[difficulty]
    number = random.randint(low, high)

    print(f"{difficulty.upper()} mode | Range: {low}-{high} | Tries: {tries}")

    for attempt in range(1, tries + 1):
        guess = int(input(f"Attempt {attempt}/{tries}: "))

        if guess == number:
            score = tries - attempt + 1
            print(f"Correct! Score: {score}")
            return score
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Game over. Number was {number}")
    return 0

total_score = 0
while True:
    diff = input("Choose difficulty (easy/medium/hard) or quit: ").lower()
    if diff == "quit":
        print(f"Final Score: {total_score}")
        break
    if diff in ["easy", "medium", "hard"]:
        total_score += play_game(diff)
    else:
        print("Invalid choice.")