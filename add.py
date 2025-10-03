import random

def get_user_guess():
    try:
        guess = int(input("Guess (1-5): "))
        if guess < 1 or guess > 5:
            raise ValueError("Guess must be between 1 and 5.")
        return guess
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    num = random.randint(1, 5)
    guess = None
    while guess is None:
        guess = get_user_guess()
    
    print("Correct!" if guess == num else f"Wrong, it was {num}")

if __name__ == "__main__":
    main()