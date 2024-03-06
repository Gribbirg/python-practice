from v1 import main as main1
from v2 import main as main2
from v3 import main as main3
from v4 import main as main4
from v5 import main as main5


def test(main):
    print(main)
    print(main([2004, 1979, 1984, 'BRO', 'IO']), "== 9")
    print(main([1975, 2005, 1980, 'BRO', 'RED']), "== 8")
    print(main([1975, 2005, 1980, 'YACC', 'RED']), "== 3")
    print(main([1978, 2005, 1980, 'OPA', 'IO']), "== 7")
    print(main([1978, 2005, 2018, 'YACC', 'RED']), "== 2")
    print(main([1978, 2005, 1980, 'YACC', 'RED']), "== 1")
    print(main([2004, 2005, 1980, 'YACC', 'IO']), "== 5")


if __name__ == '__main__':
    test(main1)
    test(main2)
    test(main3)
    test(main4)
    test(main5)
