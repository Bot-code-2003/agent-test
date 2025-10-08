import random

def get_user_guess():
    """Get a valid guess from the user."""
    while True:
        try:
            guess = int(input("Guess (1-5): "))
            if 1 <= guess <= 5:
                return guess
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

num = random.randint(1, 5)
guess = get_user_guess()

print("Correct!" if guess == num else f"Wrong, it was {num}")