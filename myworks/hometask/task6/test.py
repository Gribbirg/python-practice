from v1 import main as main1


def test(main):
    print(main({38, -24, -22, 44, -14, 84, 85, -72, 56, -1}), "==", -252)
    print(main({99, 5, -89, -18, 49, -13, 21, 56, 58, 91}), "==", -477)


if __name__ == '__main__':
    test(main1)
