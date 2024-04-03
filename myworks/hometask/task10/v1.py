def get_sorted_list(table_in):
    table = sorted(
        table_in,
        key=lambda line: "`" if line[0] is None else line[2]
    )
    table = list(filter(lambda line: line[0] is not None, table))
    res = []
    for line in table:
        if line not in res:
            res.append(line)
    return res


def first_column(table_in):
    table = []
    table_temp = []
    for i in range(len(table_in)):
        table_temp.append(table_in[i][0])
        table.append(table_in[i][0].split("@")[0])
    return table


def second_column(table_in):
    table = []
    table_temp = []
    for i in range(len(table_in)):
        table_temp.append(table_in[i][1])
        table.append(table_in[i][1] + "00")
    return table


def third_column(table_in):
    table = []
    table_temp = []
    for i in range(len(table_in)):
        table_temp.append(table_in[i][2])
        table.append(
            table_in[i][2][:13] +
            "-" +
            table_in[i][2][13:]
        )
    return table


def main(table_in):
    table_in_sorted = get_sorted_list(table_in)
    return [
        first_column(table_in_sorted),
        second_column(table_in_sorted),
        third_column(table_in_sorted)
    ]
