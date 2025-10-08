import math

def get_valid_number():
    """Prompt user for a valid non-negative number."""
    while True:
        try:
            num = float(input("Enter a non-negative number: "))
            if num < 0:
                print("Please enter a non-negative number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

num = get_valid_number()
sqrt = math.sqrt(num)

print(f"Square root of {num} is {sqrt:.2f}")