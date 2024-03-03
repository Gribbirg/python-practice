def step(x_list: list, tree: dict) -> int:
    for x in x_list:
        if x in tree:
            tree = tree[x]
            if isinstance(tree, int):
                return tree
            else:
                return step(x_list, tree)


def main(x: list) -> int:
    tree = {
        1979: 9,
        2005: {
            'BRO': 8,
            'OPA': {
                'IO': 7,
                'RED': 6
            },
            'YACC': {
                2004: {
                    'IO': 5,
                    'RED': 4
                },
                1975: 3,
                1978: {
                    1984: 0,
                    1980: 1,
                    2018: 2
                }
            }
        }
    }
    return step(x, tree)
