import random

def get_user_input(prompt):
    try:
        guess = int(input(prompt))
        if guess < 1 or guess > 5:
            raise ValueError("Input out of range. Must be between 1 and 5.")
        return guess
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return get_user_input(prompt)

def main():
    num = random.randint(1, 5)
    guess = get_user_input("Guess (1-5): ")
    print("Correct!" if guess == num else f"Wrong, it was {num}")

if __name__ == "__main__":
    main()