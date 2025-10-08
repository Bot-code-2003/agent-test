import random

def validate_input(user_input):
    """Validates that the input is an integer within the expected range."""
    try:
        guess = int(user_input)
        if 1 <= guess <= 5:
            return guess
        else:
            print("Invalid input: Please enter a number between 1 and 5.")
            return None
    except ValueError:
        print("Invalid input: Please enter a valid number.")
        return None

num = random.randint(1, 5)
user_input = input("Guess (1-5): ")
guess = validate_input(user_input)

if guess is not None:
    print("Correct!" if guess == num else f"Wrong, it was {num}")
else:
    print("No valid guess provided.")