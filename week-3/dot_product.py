#Uses python3

import sys

def optimal_advertising(prices, clicks):
    """Finds the optimal dot product

    Args:
     prices (list): prices we can charge advertisers
     clicks (list): expected clicks per slot

    Returns:
     float: the maximum we can get from the prices-clicks
    """
    clicks = sorted(clicks, reverse=True)
    prices = sorted(prices, reverse=True)
    clicks_and_prices = zip(clicks, prices)
    return sum(click * price for click, price in clicks_and_prices)

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(optimal_advertising(a, b))
    
