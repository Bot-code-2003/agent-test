import random

# Generate a random number between 1 and 5
num = random.randint(1, 5)

# Input validation for the user's guess
try:
    guess = int(input("Guess (1-5): "))
    if guess < 1 or guess > 5:
        print("Please enter a number between 1 and 5.")
    else:
        print("Correct!" if guess == num else f"Wrong, it was {num}")
except ValueError:
    print("Invalid input. Please enter a number.")