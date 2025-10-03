import random

def get_user_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_input(prompt)

num = random.randint(1, 5)
guess = get_user_input("Guess (1-5): ")

print("Correct!" if guess == num else f"Wrong, it was {num}")