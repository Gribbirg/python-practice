def main(n):
    return -0.72 if n == 0 else \
        (43 * main(n - 1) - main(n - 1) ** 3) / 61 + main(n - 1)
