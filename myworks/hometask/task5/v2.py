from math import sin, ceil


def main(y: list[float], z: list[float]) -> float:
    res = .0
    n = len(y)
    for i in range(1, n + 1):
        res += (68 *
                sin(
                    56 + z[n - i] ** 2 + 17 * y[n - ceil(i / 2)] ** 3
                ) ** 6)
    return res
