class MealyError(Exception):
    def __init__(self, fun):
        self.fun = fun


class Mealy(object):
    _ROUTES = {
        "jog": {
            "A": ("B", 0),
            "B": ("C", 1),
            "C": ("D", 3),
        },
        "peek": {
            "B": ("B", 2),
            "C": ("C", 4),
            "E": ("E", 7),
            "F": ("C", 8),
        },
        "model": {
            "D": ("E", 5),
            "E": ("F", 6),
        }
    }

    def __init__(self):
        self.currentState = 'A'

    def call_by_name(self, name):
        if self.currentState in Mealy._ROUTES[name].keys():
            res = Mealy._ROUTES[name][self.currentState]
            self.currentState = res[0]
            return res[1]
        raise MealyError(name)

    def jog(self):
        return self.call_by_name("jog")

    def peek(self):
        return self.call_by_name("peek")

    def model(self):
        return self.call_by_name("model")


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
