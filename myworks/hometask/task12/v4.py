from struct import unpack


def readA(bin, offset):
    data = dict()
    data['A1'], offset = readB(bin, offset)
    data['A2'] = unpack('i', bin[offset:offset + 4])[0]
    offset += 4
    data['A3'] = unpack('B', bin[offset:offset + 1])[0]
    offset += 1
    a4 = []
    for _ in range(2):
        adr = unpack('I', bin[offset:offset + 4])[0]
        offset += 4
        a4.append(readC(bin, adr)[0])
    data['A4'] = a4
    a5size = unpack('H', bin[offset:offset + 2])[0]
    offset += 2
    a5adr = unpack('I', bin[offset:offset + 4])[0]
    offset += 4
    a5 = []
    for _ in range(a5size):
        a5.append(unpack('f', bin[a5adr:a5adr + 4])[0])
        a5adr += 4
    data['A5'] = a5
    return data


def readB(bin, offset):
    data = dict()
    b1size = unpack('H', bin[offset:offset + 2])[0]
    offset += 2
    b1adr = unpack('I', bin[offset:offset + 4])[0]
    offset += 4
    b1 = ""
    for _ in range(b1size):
        b1 += unpack('c', bin[b1adr:b1adr + 1])[0].decode('utf-8')
        b1adr += 1
    data['B1'] = b1
    data['B2'] = unpack('B', bin[offset:offset + 1])[0]
    offset += 1
    return data, offset


def readC(bin, offset):
    data = dict()
    c1 = []
    for _ in range(3):
        c1.append(unpack("< Q", bin[offset:offset + 8])[0])
        offset += 8
    data['C1'] = c1
    data['C2'] = unpack('h', bin[offset:offset + 2])[0]
    offset += 2
    data['C3'], offset = readD(bin, offset)
    data['C4'] = unpack('q', bin[offset:offset + 8])[0]
    offset += 8
    return data, offset


def readD(bin, offset):
    data = dict()
    data['D1'] = unpack('i', bin[offset:offset + 4])[0]
    offset += 4
    data['D2'] = unpack('f', bin[offset:offset + 4])[0]
    offset += 4
    d3 = []
    for _ in range(5):
        d3.append(unpack('b', bin[offset:offset + 1])[0])
        offset += 1
    data['D3'] = d3
    return data, offset


def main(data):
    return readA(data, 4)
