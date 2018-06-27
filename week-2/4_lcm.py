# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

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

def lcm_gcd(a, b):
    """Finds the least common multiple of two integers

    Args:
     a, b: integers greater than or equal to 1
    """
    return a * b//greatest_common_divisor(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_gcd(a, b))

