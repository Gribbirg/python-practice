from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order="<"):
        self.data = data
        self.offset = offset
        self.order = order

    def jump(self, offset):
        return BinaryReader(self.data, offset, self.order)

    def read(self, pattern):
        data = unpack_from(self.order + pattern, self.data, self.offset)
        self.offset += calcsize(pattern)
        return data[0]


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.int32)
    d2 = reader.read(Types.float)
    d3 = [reader.read(Types.int8) for _ in range(5)]
    return dict(D1=d1, D2=d2, D3=d3)


def read_c(reader: BinaryReader):
    c1 = [reader.read(Types.uint64) for _ in range(3)]
    c2 = reader.read(Types.int16)
    c3 = read_d(reader)
    c4 = reader.read(Types.int64)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader: BinaryReader):
    b1size = reader.read(Types.uint16)
    b1addr = reader.read(Types.uint32)
    b1reader = reader.jump(b1addr)
    b1 = ''.join([
        b1reader.read(Types.char).decode("utf-8")
        for _ in range(b1size)
    ])
    b2 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2)


def read_a(reader: BinaryReader):
    a1 = read_b(reader)
    a2 = reader.read(Types.int32)
    a3 = reader.read(Types.uint8)
    a4 = []
    for _ in range(2):
        a4addr = reader.read(Types.uint32)
        a4reader = reader.jump(a4addr)
        a4.append(read_c(a4reader))
    a5size = reader.read(Types.uint16)
    a5addr = reader.read(Types.uint32)
    a5reader = reader.jump(a5addr)
    a5 = [a5reader.read(Types.float) for _ in range(a5size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5)


def main(bytes):
    reader = BinaryReader(bytes, 4)
    return read_a(reader)
