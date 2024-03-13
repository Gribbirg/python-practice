def main(data: list[(str, str)]) -> int:
    m = get_map(data)
    return get_code(m['D2'], m['D3'], m['D4'], m['D5'])


def get_map(data: list[(str, str)]) -> dict:
    m = {}
    for field, value in data:
        m[field] = int(value, 16)
    return m


def get_code(d2, d3, d4, d5):
    return (d5 << 18) | (d4 << 9) | (d3 << 8) | (d2 << 5)
