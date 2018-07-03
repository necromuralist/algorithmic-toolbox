# Uses python3
import sys

def get_change(money):
    coins = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money >= 5:
            money -= 5
        else:
            money -= 1
        coins += 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
