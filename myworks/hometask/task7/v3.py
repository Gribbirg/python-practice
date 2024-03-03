def main(x: list) -> int:
    tree = {
        x[1] == 1979: 9,
        x[1] == 2005: {
            x[3] == 'BRO': 8,
            x[3] == 'OPA': {
                x[4] == 'IO': 7,
                x[4] == 'RED': 6
            },
            x[3] == 'YACC': {
                x[0] == 2004: {
                    x[4] == 'IO': 5,
                    x[4] == 'RED': 4
                },
                x[0] == 1975: 3,
                x[0] == 1978: {
                    x[2] == 1984: 0,
                    x[2] == 1980: 1,
                    x[2] == 2018: 2
                }
            }
        }
    }
    while type(tree) is dict:
        tree = tree[True]
    return tree
