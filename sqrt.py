import math

def validate_input(num):
    """Validates the input to ensure it is a positive number."""
    try:
        num = float(num)
        if num < 0:
            raise ValueError("Number must be non-negative.")
        return num
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Input with validation
num = None
while num is None:
    user_input = input("Enter a number: ").strip()
    num = validate_input(user_input)

# Calculate and display the square root
sqrt = math.sqrt(num)
print("Square root of", num, "is", sqrt)