class Node:
    def __init__(self, value, conds=(), childrens=()):
        self.conds = conds
        self.childrens = childrens
        self.value = value

    def sol(self):
        if len(self.childrens) == 0:
            return self.value
        for num, c in enumerate(self.conds):
            if c == self.value:
                return self.childrens[num].sol()


def main(x):
    return Node(
        value=x[1],
        conds=(1979, 2005),
        childrens=(
            Node(value=9),
            Node(
                value=x[3],
                conds=('BRO', 'OPA', 'YACC'),
                childrens=(
                    Node(value=8),
                    Node(
                        value=x[4],
                        conds=('RED', 'IO'),
                        childrens=(
                            Node(value=6),
                            Node(value=7)
                        )
                    ),
                    Node(
                        value=x[0],
                        conds=(2004, 1975, 1978),
                        childrens=(
                            Node(
                                value=x[4],
                                conds=('RED', 'IO'),
                                childrens=(
                                    Node(value=4),
                                    Node(value=5)
                                )
                            ),
                            Node(value=3),
                            Node(
                                value=x[2],
                                conds=(2018, 1980, 1984),
                                childrens=(
                                    Node(value=2),
                                    Node(value=1),
                                    Node(value=0)
                                )
                            )
                        )
                    )
                )
            )
        )
    ).sol()
