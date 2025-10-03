import random

def get_validated_input(prompt):
    try:
        user_input = int(input(prompt))
        if user_input < 1 or user_input > 5:
            raise ValueError("Input out of range.")
        return user_input
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return get_validated_input(prompt)

num = random.randint(1, 5)
guess = get_validated_input("Guess (1-5): ")

print("Correct!" if guess == num else f"Wrong, it was {num}")