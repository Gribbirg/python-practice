def main(table_in):
    table = table_in.copy()
    table = remove_duplicates(table)
    table = list(filter(
        lambda line: not all(map(lambda element: element is None, line)),
        table
    ))
    table = change_elements(table)
    table.sort(key=lambda line: line[2])
    return [
        [
            table[j][i]
            for j in range(len(table))
        ]
        for i in range(len(table[0]))
    ]


def remove_duplicates(table):
    res = []
    for line in table:
        if line not in res:
            res.append(line)
    return res


def change_elements(table):
    for line in table:
        line[0] = line[0].split("@")[0]
        line[1] = f"{float(line[1]):.3f}"
        line[2] = line[2][:13] + "-" + line[2][13:]
    return table
