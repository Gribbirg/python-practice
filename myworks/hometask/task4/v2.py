def main(n):
    if n == 0:
        return -.72

    prev = main(n - 1)
    return (43 * prev - prev ** 3) / 61 + prev
