def main(x: list) -> int:
    return x1(x)


def x0(x: list) -> int:
    match x[0]:
        case 2004:
            return x4(x, 4)
        case 1975:
            return 3
        case _:
            return x2(x)


def x1(x: list) -> int:
    match x[1]:
        case 1979:
            return 9
        case _:
            return x3(x)


def x2(x: list) -> int:
    match x[2]:
        case 2018:
            return 2
        case 1980:
            return 1
        case _:
            return 0


def x3(x: list) -> int:
    match x[3]:
        case 'BRO':
            return 8
        case 'OPA':
            return x4(x, 6)
        case _:
            return x0(x)


def x4(x: list, start: int) -> int:
    match x[4]:
        case 'RED':
            return start
        case _:
            return start + 1
