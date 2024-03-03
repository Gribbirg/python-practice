def main(x: list) -> int:
    return x1(x)


def x0(x: list) -> int:
    return x4(x, 4) if x[0] == 2004 else 3 if x[0] == 1975 else x2(x)


def x1(x: list) -> int:
    return 9 if x[1] == 1979 else x3(x)


def x2(x: list) -> int:
    return 2 if x[2] == 2018 else 1 if x[2] == 1980 else 0


def x3(x: list) -> int:
    return 8 if x[3] == 'BRO' else x4(x, 6) if x[3] == 'OPA' else x0(x)


def x4(x: list, start: int) -> int:
    return start if x[4] == 'RED' else start + 1
