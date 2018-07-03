# Uses python3
import sys

def maximize_loot(capacity, weights, values):
    """Figure out the maximum value the thief can haul off

    Args:
     capacity (int): number of pounds backpack can hold
     weights (list): how many pounds of each item there is
     values (list): how much each item is worth per pound

    Raises:
     AssertionError: weights and values are different lengths

    Returns:
     float: max-value the backpack can hold
    """
    weight_count = len(weights)
    assert weight_count == len(values), \
        "Weights and Values not same shape: weights={} values={}".format(
            weight_count, len(values))
    values_per_pound = ((values[index]/weights[index], index)
                        for index in range(weight_count))

    # we have to reverse-sort it (otherwise sorting puts the smallest
    # number first)
    per_poundage = sorted(values_per_pound, reverse=True)

    # loot is the value of what we've taken so far
    loot = 0

    # precondition: per_poundage is the value-per-pound in descending
    # order for each item along with the index of the original weight/value
    for value, index in per_poundage:
        # invariant: value is the largest price-per-pound available
        if capacity < weights[index]:
            # we don't have enough strength to take all of this item
            # so just take as much as we can and quit
            loot += value * capacity
            break
        # otherwise take all of this item
        loot += values[index]
        # reducing our capacity by its total weight
        capacity -= weights[index]
        if capacity == 0:
            # we're out of capacity, quit
            break
    return loot


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = maximize_loot(capacity, weights, values)
    print("{:.10f}".format(opt_value))
