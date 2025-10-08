import math

def validate_input(value):
    """Validate that the input is a positive number."""
    try:
        number = float(value)
        if number >= 0:
            return number
    except ValueError:
        pass
    return None

num = input("Enter a positive number: ")
validated_num = validate_input(num)

if validated_num is not None:
    sqrt = math.sqrt(validated_num)
    print(f"Square root of {validated_num} is {sqrt}")
else:
    print("Invalid input. Please enter a positive number.")