from math import sin, ceil


def main(y: list[float], z: list[float]) -> float:
    return sum([
        68 *
        sin(56 + z[len(y) - i] ** 2 + 17 * y[len(y) - ceil(i / 2)] ** 3) ** 6
        for i in range(1, len(y) + 1)
    ])
