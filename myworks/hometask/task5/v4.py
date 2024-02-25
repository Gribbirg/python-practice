from math import sin, ceil


def main(y: list[float], z: list[float], i: int = 1) -> float:
    if i == len(y) + 1:
        return 0
    return (68 *
            sin(
                56 + z[len(y) - i] ** 2 + 17 * y[len(y) - ceil(i / 2)] ** 3
            ) ** 6 +
            main(y, z, i + 1))
