def main(n):
    value = -0.72
    for _ in range(n):
        value = (43 * value - value ** 3) / 61 + value
    return value
