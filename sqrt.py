import math

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return get_number(prompt)

num = get_number("Enter a number: ")
sqrt = math.sqrt(num)

print("Square root of", num, "is", sqrt)