import random

def validate_guess(guess):
    """Validate that the guess is an integer within the allowed range."""
    try:
        guess = int(guess)
        if 1 <= guess <= 5:
            return guess
    except ValueError:
        pass
    return None

num = random.randint(1, 5)
guess = input("Guess (1-5): ")
validated_guess = validate_guess(guess)

if validated_guess is not None:
    print("Correct!" if validated_guess == num else f"Wrong, it was {num}")
else:
    print("Invalid input. Please enter a number between 1 and 5.")