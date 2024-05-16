import struct


def D(x, i):
    return {
        "D1": struct.unpack("< i", x[i: i + 4])[0],
        "D2": struct.unpack("< f", x[i + 4: i + 8])[0],
        "D3": [
            struct.unpack('< b', x[i + 8 + j: i + 9 + j])[0]
            for j in range(5)
        ],
    }


def C(x, i):
    return {
        'C1': [
            struct.unpack("< Q", x[i + j * 8: i + 8 + j * 8])[0]
            for j in range(3)
        ],
        'C2': struct.unpack("< h", x[i + 24: i + 26])[0],
        'C3': D(x, i + 26),
        'C4': struct.unpack("< q", x[i + 39: i + 47])[0],
    }


def B(x, i):
    size = struct.unpack("< H", x[i: i + 2])[0]
    address = struct.unpack("< I", x[i + 2: i + 6])[0]
    return {
        "B1": struct
        .unpack(f"< {size}s", x[address: address + size])[0]
        .decode("utf-8"),
        "B2": struct.unpack("< B", x[i + 6: i + 7])[0],
    }


def A(x, i):
    size = struct.unpack("< H", x[i + 20: i + 22])[0]
    address = struct.unpack("< I", x[i + 22: i + 26])[0]
    return {
        'A1': B(x, i),
        'A2': struct.unpack('< i', x[i + 7: i + 11])[0],
        'A3': struct.unpack('< B', x[i + 11: i + 12])[0],
        'A4': [
            C(x, struct.unpack("< I", x[i + 12 + j * 4: i + 16 + j * 4])[0])
            for j in range(2)
        ],
        'A5': [
            struct.unpack('< f', x[address + j * 4: address + 4 + j * 4])[0]
            for j in range(size)
        ],
    }


def main(x):
    return A(x, 4)
