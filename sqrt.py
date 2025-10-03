import math

try:
    # Validate and sanitize user input
    num = input("Enter a number: ")
    if not num.replace('.', '', 1).isdigit() or num.count('.') > 1:
        raise ValueError("Input must be a numeric value.")
    
    num = float(num)
    if num < 0:
        raise ValueError("Number must be non-negative.")

    # Calculate square root
    sqrt = math.sqrt(num)

    # Output the result
    print("Square root of", num, "is", sqrt)
except ValueError as e:
    print(f"Error: {e}")