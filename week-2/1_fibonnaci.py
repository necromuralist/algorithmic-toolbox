# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fibonacci_iterative(n):
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

n = int(input())
print(fibonacci_iterative(n))
