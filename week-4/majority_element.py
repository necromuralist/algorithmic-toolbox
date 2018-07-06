# Uses python3
import sys
from collections import defaultdict

class Outcome:
    has_majority = 1
    no_majority = 0

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def naive_majority(voters):
    """Decides if there is a majority element

    Args:
     voters: list of elements to check

    Returns:
     int: 1 if there is a majority element, 0 otherwise
    """
    half = len(voters)//2
    for index, voter in enumerate(voters):
        count = 0
        for other_voter in voters:
            if voter == other_voter:
                count += 1
        if count > half:
            return Outcome.has_majority
    return Outcome.no_majority

def iterative_majority(votes):
    """Decides if there is a majority among the votes

    Args:
     votes (list): collection to check

    Returns:
     int: 1 if there is a majority, 0 otherwise
    """
    half = len(votes)//2
    counts = defaultdict(lambda: 0)
    for vote in votes:
        counts[vote] += 1

    sorted_counts = sorted((count for count in counts.values()), reverse=True)
    return (Outcome.has_majority if sorted_counts[0] > half
            else Outcome.no_majority)

def iterative_majority_two(votes):
    """Decides if there is a majority among the votes

    Args:
     votes (list): collection to check

    Returns:
     int: 1 if there is a majority, 0 otherwise
    """
    half = len(votes)//2
    counts = defaultdict(lambda: 0)
    for vote in votes:
        counts[vote] += 1

    for count in counts.values():
        if count > half:
            return Outcome.has_majority
    return Outcome.no_majority

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(iterative_majority_two(a))
