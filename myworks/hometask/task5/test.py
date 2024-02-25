from myworks.hometask.task5.v1 import main as main1
from myworks.hometask.task5.v2 import main as main2
from myworks.hometask.task5.v3 import main as main3
from myworks.hometask.task5.v4 import main as main4


def test(main):
    print(main)
    print(main([-0.11, 0.99, 0.44], [-0.15, -0.19, 1.0]))
    print(main([-0.56, -0.99, -0.03], [-0.42, 0.64, -0.27]))
    print(main([-0.18, 0.14, -0.84], [-0.23, -0.47, -0.46]))
    print(main([-0.37, 0.99, 0.74], [-0.47, -0.32, -0.92]))
    print(main([0.69, 0.35, -0.48], [0.14, 0.9, 0.81]))


if __name__ == '__main__':
    test(main1)
    test(main2)
    test(main3)
    test(main4)
