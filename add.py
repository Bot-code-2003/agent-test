# guess_number_game.py
import random

def validate_guess(guess):
    """Validates that the guess is within the acceptable range."""
    try:
        guess_int = int(guess)
        if 1 <= guess_int <= 5:
            return guess_int
        else:
            print("Error: Guess must be between 1 and 5.")
            return None
    except ValueError:
        print("Error: Invalid input, please enter a number.")
        return None

# Generate random number
num = random.randint(1, 5)

# User input with validation
guess = None
while guess is None:
    user_input = input("Guess (1-5): ").strip()
    guess = validate_guess(user_input)

# Result
print("Correct!" if guess == num else f"Wrong, it was {num}")