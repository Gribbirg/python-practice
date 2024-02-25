import math


def main(m, a, n, z):
    res = 0

    j = 1
    while j <= m:
        res += (math.log10(j ** 2 + j + j ** 3)) ** 4
        j += 1

    j = 1
    while j <= n:
        c = 1
        while c <= a:
            i = 1
            while i <= m:
                res -= (i ** 3 - c) ** 7 - \
                       43 * math.acos(z) - \
                       (math.log10(j) ** 6)
                i += 1
            c += 1
        j += 1

    return res
