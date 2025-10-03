import random

def sanitize_input(prompt, valid_range):
    try:
        guess = int(input(prompt))
        if guess in valid_range:
            return guess
        else:
            print(f"Please enter a number in the range {valid_range}.")
            return sanitize_input(prompt, valid_range)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return sanitize_input(prompt, valid_range)

num = random.randint(1, 5)
guess = sanitize_input("Guess (1-5): ", range(1, 6))

print("Correct!" if guess == num else f"Wrong, it was {num}")