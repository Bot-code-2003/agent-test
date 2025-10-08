import math

def validate_input(user_input):
    """Validates that the input is a positive number."""
    try:
        num = float(user_input)
        if num >= 0:
            return num
        else:
            print("Invalid input: Please enter a non-negative number.")
            return None
    except ValueError:
        print("Invalid input: Please enter a valid number.")
        return None

user_input = input("Enter a number: ")
num = validate_input(user_input)

if num is not None:
    sqrt = math.sqrt(num)
    print("Square root of", num, "is", sqrt)
else:
    print("No valid input provided.")