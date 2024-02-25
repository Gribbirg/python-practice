from math import cos


def main(x):
    res_map = {
        x < 169: lambda y: y ** 7 + y ** 6,
        169 <= x < 264: lambda y: 97 * (cos(82 * y ** 2 + y ** 3)) ** 2,
        x >= 264: lambda y:
        97 * (y ** 2 + y / 76 + 98 * y ** 3) ** 7 - y ** 3 - y / 94
    }
    for condition, fun in res_map.items():
        if condition:
            return fun(x)
