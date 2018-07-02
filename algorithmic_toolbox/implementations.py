# from pypi
from joblib import Memory

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

def fibonacci(n):
    """Calculates the nth fibonacci number

    Args:
     n (int): the fibonacci number to get (e.g. 3 means third)

    Returns:
     int: nth fibonacci number
    """
    first = (0, 1)
    if n in first:
        return n
    previous, current = first
    for index in range(2, n + 1):
        previous, current = current, previous + current
    return current

memory = Memory(location="/tmp/memories/")

@memory.cache
def fibonacci_cached(n):
    """Calculates the nth fibonacci number

    Args:
     n (int): the fibonacci number to get (e.g. 3 means third)

    Returns:
     int: nth fibonacci number
    """
    first = (0, 1)
    if n in first:
        return n
    previous, current = first
    for index in range(2, n + 1):
        previous, current = current, previous + current
    return current
