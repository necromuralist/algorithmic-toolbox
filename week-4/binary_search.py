# Uses python3
import sys

NOT_FOUND = -1

def binary_search(K, q):
    """Finds the index of an item in the list

    Args:
     K (list): A sorted list of integers
     q (int): the item to search for
    
    Returns:
     int: index of q in K or -1 if not found
    """
    min_index, max_index = 0, len(K) - 1
    counter = 0
    while max_index >= min_index:
        mid_index = (min_index + max_index)//2

        if K[mid_index] == q:
            return mid_index
        elif K[mid_index] < q:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    return NOT_FOUND

def multiple_search(source, keys):
    """Searches the source for the keys

    Args:
     source (list): sorted list of search items
     keys (list): items to search for in the source

    Returns:
     list: indices of keys in source
    """
    return [binary_search(source, key) for key in keys]

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
