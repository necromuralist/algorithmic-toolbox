# python3
# Maximum Pairwise Product Problem
# Find the maximum product of two distinct numbers in a sequence of non-negative integers.
# Input: A sequence of non-negative integers.
# Output: The maximum value that can be obtained by multiplying two different elements from the sequence. 
# 5
# 6
# 2
# 7
# 4
# 5 6
# 30
# 30
# 10 12
# 35 42
# 20 24
# 2 7 4
# 10 35 20
# 12 42 24
# 7 4
# 28
# 14
# 8 28
# Given a sequence of non-negative integers a 1 , . . . , a n , compute

# max a i · a j .
# 1≤i,j≤n

def max_pairwise_product_brute(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_take_two(numbers):
    """Finds the maximum pairwise product in te numbers
    
    Args:
     numbers (list): non-negative integers

    Returns:
     int: largest possible product from the numbers
    """    
    first_index = 0
    first_value = 0
    n = len(numbers)
    assert n >= 2
    for index in range(1, n):
        if numbers[index] > first_value:
            first_value = numbers[index]
            first_index = index

    second_value = 0
    start = 1 if first_index == 0 else 0
    for index in range(start, n):
        if index != first_index and numbers[index] > second_value:
            second_value = numbers[index]
    return first_value * second_value

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_take_two(input_numbers))
