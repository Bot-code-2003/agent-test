import math

def sqrt(x: float) -> float:
    """
    Calculate the square root of a non-negative number.

    Args:
        x (float): A non-negative number to calculate the square root for.

    Returns:
        float: The square root of x.

    Raises:
        ValueError: If x is negative.
        TypeError: If x is not a number.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Input must be a number, got {type(x).__name__}")
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    return math.sqrt(x)
