import math

def get_valid_number():
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return num
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_valid_number()

num = get_valid_number()
sqrt = math.sqrt(num)

print("Square root of", num, "is", sqrt)