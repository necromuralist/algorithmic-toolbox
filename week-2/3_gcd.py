# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_modulus(a, b):
    """finds the GCD of a and b

    Args:
     a, b: non-negative integers

    Returns:
     int: the GCD of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_modulus(a, b))
