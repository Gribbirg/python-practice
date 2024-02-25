def main(n):
    n_list = [-.72]
    for i in range(1, n + 1):
        n_list.append(
            (43 * n_list[i - 1] - n_list[i - 1] ** 3) /
            61 + n_list[i - 1]
        )
    return n_list[n]
