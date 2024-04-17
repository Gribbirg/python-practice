class MealyError(Exception):
    def __init__(self, fun):
        self.fun = fun


class Mealy(object):
    def __init__(self):
        self.currentState = 'A'

    def jog(self):
        match self.currentState:
            case 'A':
                self.currentState = 'B'
                return 0
            case 'B':
                self.currentState = 'C'
                return 1
            case 'C':
                self.currentState = 'D'
                return 3
            case _:
                raise MealyError("jog")

    def peek(self):
        match self.currentState:
            case 'B':
                return 2
            case 'C':
                return 4
            case 'E':
                return 7
            case 'F':
                self.currentState = 'C'
                return 8
            case _:
                raise MealyError("peek")

    def model(self):
        match self.currentState:
            case 'D':
                self.currentState = 'E'
                return 5
            case 'E':
                self.currentState = 'F'
                return 6
            case _:
                raise MealyError("model")


def main():
    return Mealy()


def test_raise(fun):
    res = None
    try:
        res = fun()
    except MealyError as e:
        assert e.fun == fun.__name__
    assert res is None


def test():
    o = main()
    assert o.jog() == 0
    assert o.peek() == 2
    assert o.jog() == 1
    assert o.peek() == 4
    assert o.jog() == 3
    assert o.model() == 5
    assert o.peek() == 7
    assert o.model() == 6
    assert o.peek() == 8

    test_raise(o.model)
    o.jog()
    test_raise(o.jog)
    test_raise(o.peek)
