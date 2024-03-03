from v1 import main as main1
from v2 import main as main2


def test(main):
    print(main)
    print(main([2004, 1979, 1984, 'BRO', 'IO']), "== 9")
    print(main([1975, 2005, 1980, 'BRO', 'RED']), "== 8")
    print(main([1975, 2005, 1980, 'YACC', 'RED']), "== 3")
    print(main([1978, 2005, 1980, 'OPA', 'IO']), "== 7")
    print(main([1978, 2005, 2018, 'YACC', 'RED']), "== 2")


if __name__ == '__main__':
    test(main1)
    test(main2)
