import random

# Generate a random number between 1 and 5
num = random.randint(1, 5)

# Input validation and sanitization
try:
    guess = int(input("Guess (1-5): ").strip())
    if guess < 1 or guess > 5:
        raise ValueError("Input out of range.")
except ValueError:
    print("Invalid input! Please enter a number between 1 and 5.")
else:
    # Compare the guess with the random number
    print("Correct!" if guess == num else f"Wrong, it was {num}")