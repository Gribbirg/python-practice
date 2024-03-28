from v1 import main as main1


def test(main):
    print(main(
        [
            ["kefic15@rambler.ru", "0.5", "+7 227 032-6764"],
            ["sizavanz13@rambler.ru", "0.8", "+7 152 957-7564"],
            ["rovutak66@yahoo.com", "0.1", "+7 674 104-5872"],
            [None, None, None],
            ["ruzugev97@gmail.com", "0.3", "+7 900 864-2212"],
            ["ruzugev97@gmail.com", "0.3", "+7 900 864-2212"],
            ["ruzugev97@gmail.com", "0.3", "+7 900 864-2212"]
        ]
    ))


if __name__ == '__main__':
    test(main1)
