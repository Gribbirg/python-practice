import math


def main(y, z):
    x = (97 * (z ** 2 + y / 76 + 98 * y ** 3) ** 7 + z) ** 0.5
    x1 = 70 * (y + 66 * z ** 3) ** 2 + math.fabs(y)
    x2 = (y ** 2 - y) ** 6
    x3 = (z ** 2 / 87 - 79 * y - 53 * z ** 3)

    x4 = x1 / (x2 + x3 ** 3)

    return x + x4
