def add_numbers(a: float, b: float) -> float:
    """
    Returns the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        TypeError: If either input is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers (int or float).")
    return a + b
