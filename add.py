import random

def main():
    try:
        num = random.randint(1, 5)
        guess = int(input("Guess a number between 1 and 5: "))
        
        if guess < 1 or guess > 5:
            print("Invalid input. Please enter a number between 1 and 5.")
        else:
            print("Correct!" if guess == num else f"Wrong, it was {num}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
