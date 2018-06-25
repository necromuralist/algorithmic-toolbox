# first line: 1
@memory.cache
def reference_implementation(n):
    """Calculates the nth fibonacci number

    Args:
     n (int): the fibonacci number to get (e.g. 3 means third)

    Returns:
     int: nth fibonacci number
    """
    if (n <= 1):
        return n
    return (calculate_fibonacci_recursive(n - 1)
            + calculate_fibonacci_recursive(n - 2))
