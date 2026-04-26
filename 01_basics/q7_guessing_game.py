# Q7 - Number Guessing Game
import random

def play_game(difficulty):
    levels = {
        "easy": (1, 50, 10),
        "medium": (1, 100, 7),
        "hard": (1, 200, 5)
    }
    
    low, high, tries = levels[difficulty]
    number = random.randint(low, high)
    score = 0

    print(f"\n🎮 {difficulty.upper()} mode | Range: {low}-{high} | Tries: {tries}")
    
    for attempt in range(1, tries + 1):
        guess = int(input(f"Attempt {attempt}/{tries} → Your guess: "))
        
        if guess == number:
            score = tries - attempt + 1
            print(f"🎉 Correct! Score: {score}")
            return score
        elif guess < number:
            print("📈 Too low!")
        else:
            print("📉 Too high!")
    
    print(f"💀 Game Over! Number was {number}")
    return 0

# Main
total_score = 0
while True:
    diff = input("\nChoose difficulty (easy/medium/hard) or 'quit': ").lower()
    if diff == 'quit':
        print(f"🏆 Final Score: {total_score}")
        break
    if diff in ["easy", "medium", "hard"]:
        total_score += play_game(diff)
    else:
        print("Invalid choice!")