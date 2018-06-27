def greatest_common_divisor(a, b):
    """finds the GCD of a and b

    Args:
     a, b: non-negative integers

    Returns:
     int: the GCD of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a
