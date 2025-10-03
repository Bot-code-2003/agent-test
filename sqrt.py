import math
import logging

# Configure logging for user interactions
logging.basicConfig(level=logging.INFO, filename='sqrt_calculations.log', format='%(asctime)s - %(message)s')

def validate_input(user_input):
    try:
        user_input = float(user_input)
        if user_input < 0:
            raise ValueError("Negative numbers are not allowed.")
        return user_input
    except ValueError:
        logging.warning(f"Invalid input provided: {user_input}")
        return None

def main():
    num = input("Enter a number: ")
    validated_num = validate_input(num)

    if validated_num is None:
        print("Invalid input. Please enter a non-negative number.")
    else:
        sqrt = math.sqrt(validated_num)
        logging.info(f"Square root calculated for {validated_num}: {sqrt}")
        print("Square root of", validated_num, "is", sqrt)

if __name__ == "__main__":
    main()