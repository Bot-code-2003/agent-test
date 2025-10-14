import math

def sqrt(number: float) -> float:
    """
    Calculate the square root of a non-negative number.

    Args:
        number (float): A non-negative number to calculate the square root of.

    Returns:
        float: The square root of the input number.

    Raises:
        ValueError: If the input number is negative.
        TypeError: If the input is not a number.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a numeric type (int or float).")
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(number)
