def main(n):
    match n:
        case 0:
            return -.72
        case _:
            prev = main(n - 1)
            return (43 * prev - prev ** 3) / 61 + prev
