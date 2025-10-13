import math

def sqrt(x):
    """
    Compute the square root of a non-negative number.

    Parameters:
    x (int or float): The number to compute the square root of.

    Returns:
    float: The square root of x.

    Raises:
    TypeError: If x is not an int or float.
    ValueError: If x is negative.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an int or float")
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)
