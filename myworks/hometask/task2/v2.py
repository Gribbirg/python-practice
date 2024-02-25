import math


def main(x):
    if x < 169:
        return x ** 7 + x ** 6
    if x < 264:
        return 97 * (math.cos(82 * x ** 2 + x ** 3)) ** 2
    return 97 * (x ** 2 + x / 76 + 98 * x ** 3) ** 7 - x ** 3 - x / 94

