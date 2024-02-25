import math


def main(m, a, n, z, j=1, c=1, i=1):
    if j == n + 1:
        return 0
    elif c == a + 1:
        return main(m, a, n, z, j + 1, 1, 1)
    elif i == m + 1:
        return main(m, a, n, z, j, c + 1, 1)
    else:
        return ((math.log10(i ** 2 + i + i ** 3)) ** 4 if c == j == 1 else 0) - \
            ((i ** 3 - c) ** 7 -
             43 * math.acos(z) -
             (math.log10(j) ** 6)) + \
            main(m, a, n, z, j, c, i + 1)
