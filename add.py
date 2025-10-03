import random

def secure_input(prompt, min_val, max_val):
    try:
        guess = int(input(prompt))
        if min_val <= guess <= max_val:
            return guess
        else:
            print(f"Please enter a number between {min_val} and {max_val}.")
            return secure_input(prompt, min_val, max_val)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return secure_input(prompt, min_val, max_val)

def main():
    num = random.randint(1, 5)
    guess = secure_input("Guess (1-5): ", 1, 5)
    print("Correct!" if guess == num else f"Wrong, it was {num}")

if __name__ == "__main__":
    main()