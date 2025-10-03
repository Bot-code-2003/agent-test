import random

def get_user_input(prompt):
    """Get sanitized user input."""
    try:
        user_input = int(input(prompt))
        if 1 <= user_input <= 5:
            return user_input
        else:
            raise ValueError("Input out of range.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return get_user_input(prompt)

def main():
    num = random.randint(1, 5)
    guess = get_user_input("Guess (1-5): ")
    
    print("Correct!" if guess == num else f"Wrong, it was {num}")

if __name__ == "__main__":
    main()