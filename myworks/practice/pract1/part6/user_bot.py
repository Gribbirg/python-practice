from random import randint


def script(check, x, y):
    if check("gold", x, y) != 0:
        print(f'take gold at {x} {y}')
        return "take"

    match check("level"):
        case 3:
            if check("gold", 14, 13):
                pass
            elif check("gold", 8, 23):
                if y < 17:
                    return "down"
                if x > 10:
                    return "left"
            elif check("gold", 26, 16):
                if y > 16:
                    return "up"
                if x < 20:
                    return "right"
            elif check("gold", 19, 23):
                if y < 20:
                    return "down"

            elif check("gold", 26, 1):
                if y > 3:
                    return "up"
        case 4:
            if check("gold", 8, 16):
                if x < 5 and y < 10:
                    return "right"
                if y < 17:
                    return "down"
            elif check("gold", 1, 23):
                if x > 2:
                    return "left"
            elif check("gold", 8, 23):
                pass
            elif check("gold", 19, 16):
                if y > 19 and x < 18:
                    return "up"
                if x < 19:
                    return "right"
                if not check("wall", x, y - 1):
                    return "up"
            elif check("gold", 26, 16):
                if not check("wall", x + 1, y):
                    return "right"
            elif check("gold", 26, 23):
                if not check("wall", x, y + 1):
                    return "down"
            elif check("gold", 19, 23):
                pass
            elif check("gold", 19, 8):
                if x < 22 and y > 10:
                    return "right"
                if y > 7:
                    return "up"
                if not check("wall", x - 1, y):
                    return "left"
            elif check("gold", 19, 1):
                if not check("wall", x, y - 1):
                    return "up"
            elif check("gold", 26, 1):
                if not check("wall", x + 1, y):
                    return "right"
            elif check("gold", 26, 8):
                pass
            else:
                if x > 22 and y < 10:
                    return "left"
                if y < 12 and x > 20:
                    return "down"
        case _:
            pass

    return go_to_gold(check, x, y)


def go_to_gold(check, x, y):
    x_gold, y_gold = find_gold(check, x, y)
    return way_to_gold(check, x, y, x_gold, y_gold)


def find_gold(check, x, y, distance=0):
    for i in range(x - distance, x + distance + 1):
        for j in range(y - distance, y + distance + 1):
            if check("gold", i, j) != 0:
                return i, j
    if distance > 100:
        return find_gold(check, x, y)
    return find_gold(check, x, y, distance + 1)


def way_to_gold(check, x, y, x_gold, y_gold):
    if x_gold > x and not check("wall", x + 1, y):
        return "right"
    if x_gold < x and not check("wall", x - 1, y):
        return "left"
    if y_gold > y and not check("wall", x, y + 1):
        return "down"
    if y_gold < y and not check("wall", x, y - 1):
        return "up"
    return ["right", "left", "down", "up"][randint(0, 3)]
