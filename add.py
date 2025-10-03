import random

def validate_input(prompt):
    try:
        guess = int(input(prompt))
        if guess < 1 or guess > 5:
            raise ValueError("Input must be between 1 and 5.")
        return guess
    except ValueError as e:
        print(f"Invalid input: {e}")
        return validate_input(prompt)

def main():
    num = random.randint(1, 5)
    guess = validate_input("Guess (1-5): ")

    print("Correct!" if guess == num else f"Wrong, it was {num}")

if __name__ == "__main__":
    main()