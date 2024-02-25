import math


def main(m, a, n, z):
    res = 0

    for j in range(1, m + 1):
        res += (math.log10(j ** 2 + j + j ** 3)) ** 4

    for j in range(1, n + 1):
        for c in range(1, a + 1):
            for i in range(1, m + 1):
                res -= (i ** 3 - c) ** 7 - \
                       43 * math.acos(z) - \
                       (math.log10(j) ** 6)

    return res
