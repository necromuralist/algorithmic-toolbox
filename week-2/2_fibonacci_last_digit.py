# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

first = (0, 1)

def get_fibonacci_last_digit_modulo(n):
    if n in first:
        return n

    previous, current = first

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current % 10

if __name__ == '__main__':
    number = sys.stdin.read()
    n = int(number)
    print(get_fibonacci_last_digit_modulo(n))
