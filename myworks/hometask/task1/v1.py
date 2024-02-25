from math import fabs


def main(y, z):
    return ((97 * (z ** 2 + y / 76 + 98 * y ** 3) ** 7 + z) ** 0.5 +
            (70 * (y + 66 * z ** 3) ** 2 + fabs(y)) /
            ((y ** 2 - y) ** 6 +
             (z ** 2 / 87 - 79 * y - 53 * z ** 3) ** 3))
