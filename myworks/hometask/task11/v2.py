class MealyError(Exception):
    def __init__(self, fun):
        self.fun = fun


class Mealy(object):
    def __init__(self):
        self.currentState = 'A'

    def jog(self):
        if self.currentState == 'A':
            self.currentState = 'B'
            return 0
        if self.currentState == 'B':
            self.currentState = 'C'
            return 1
        if self.currentState == 'C':
            self.currentState = 'D'
            return 3
        raise MealyError("jog")

    def peek(self):
        if self.currentState == 'B':
            return 2
        if self.currentState == 'C':
            return 4
        if self.currentState == 'E':
            return 7
        if self.currentState == 'F':
            self.currentState = 'C'
            return 8
        raise MealyError("peek")

    def model(self):
        if self.currentState == 'D':
            self.currentState = 'E'
            return 5
        if self.currentState == 'E':
            self.currentState = 'F'
            return 6
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
