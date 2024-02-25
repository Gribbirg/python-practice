import math


def main(m, a, n, z):
    return sum(
        [(math.log10(i ** 2 + i + i ** 3)) ** 4 for i in range(1, m + 1)]) - \
        sum([(i ** 3 - c) ** 7 -
             43 * math.acos(z) -
             (math.log10(j) ** 6)
             for i in range(1, m + 1)
             for c in range(1, a + 1)
             for j in range(1, n + 1)])
