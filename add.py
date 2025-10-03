import random

def get_valid_guess():
    try:
        guess = int(input("Guess (1-5): "))
        if guess < 1 or guess > 5:
            raise ValueError("Out of range")
        return guess
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return get_valid_guess()

num = random.randint(1, 5)
guess = get_valid_guess()

print("Correct!" if guess == num else f"Wrong, it was {num}")