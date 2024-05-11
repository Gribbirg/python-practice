from struct import *

FMT = dict(
    char='c',
    int8='b',
    uint8='B',
    int16='h',
    uint16='H',
    int32='i',
    uint32='I',
    int64='q',
    uint64='Q',
    float='f',
    double='d'
)


def parse(buf, offs, ty, order='<'):
    pattern = FMT[ty]
    size = calcsize(pattern)
    value = unpack_from(order + pattern, buf, offs)[0]
    return value, offs + size


def parse_d(buf, offs):
    d1, offs = parse(buf, offs, 'int32')
    d2, offs = parse(buf, offs, 'float')
    d3 = []
    for _ in range(5):
        val, offs = parse(buf, offs, 'int8')
        d3.append(val)
    return dict(D1=d1, D2=d2, D3=d3), offs


def parse_c(buf, offs):
    c1 = []
    for _ in range(3):
        val, offs = parse(buf, offs, 'uint64')
        c1.append(val)
    c2, offs = parse(buf, offs, 'int16')
    c3, offs = parse_d(buf, offs)
    c4, offs = parse(buf, offs, 'int64')
    return dict(C1=c1, C2=c2, C3=c3, C4=c4), offs


def parse_b(buf, offs):
    b1size, offs = parse(buf, offs, 'uint16')
    b1offs, offs = parse(buf, offs, 'uint32')
    b1 = []
    for _ in range(b1size):
        val, b1offs = parse(buf, b1offs, 'char')
        b1.append(val.decode("utf-8"))
    b1 = ''.join(b1)
    b2, offs = parse(buf, offs, 'uint8')
    return dict(B1=b1, B2=b2), offs


def parse_a(buf, offs):
    a1, offs = parse_b(buf, offs)
    a2, offs = parse(buf, offs, 'int32')
    a3, offs = parse(buf, offs, 'uint8')
    a4 = []
    for _ in range(2):
        a4offs, offs = parse(buf, offs, 'uint32')
        val, a4offs = parse_c(buf, a4offs)
        a4.append(val)
    a5size, offs = parse(buf, offs, 'uint16')
    a5offs, offs = parse(buf, offs, 'uint32')
    a5 = []
    for _ in range(a5size):
        val, a5offs = parse(buf, a5offs, 'float')
        a5.append(val)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5), offs


def main(stream):
    res, _ = parse_a(stream, 4)
    return res
