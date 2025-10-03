import random

try:
    # Generate a random number securely
    num = random.randint(1, 5)
    
    # Validate user input
    guess = input("Guess (1-5): ")
    if not guess.isdigit():
        raise ValueError("Input must be a number.")

    guess = int(guess)
    if guess < 1 or guess > 5:
        raise ValueError("Number must be between 1 and 5.")

    # Output the result
    print("Correct!" if guess == num else f"Wrong, it was {num}")
except ValueError as e:
    print(f"Invalid input: {e}")