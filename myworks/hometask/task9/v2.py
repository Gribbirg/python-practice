class State:
    CLOSED = 0
    OPENED = 1
    INT = 2
    NAME = 3


class Parse:
    def __init__(self):
        self.current_name = ""
        self.current_int = ""
        self.state = State.CLOSED
        self.res = []

    def de_parse(self, s: str):
        self.res = []
        self.current_name = ""
        self.current_int = ""
        self.state = State.CLOSED

        for char in s:
            match char:
                case "<":
                    self.open_tag()
                case "'":
                    self.name_tag()
                case "#":
                    self.int_open_tag()
                case ">":
                    self.int_closed_tag()
                case _:
                    self.other_sym(char)

        return self.res

    def open_tag(self):
        if self.state == State.CLOSED:
            self.current_name = ""
            self.current_int = ""
            self.state = State.OPENED
        elif self.state == State.OPENED:
            self.res.append((self.current_name, int(self.current_int)))
            self.state = State.CLOSED

    def name_tag(self):
        if self.state == State.OPENED:
            self.state = State.NAME
        elif self.state == State.NAME:
            self.state = State.OPENED

    def int_open_tag(self):
        if self.state == State.OPENED:
            self.state = State.INT

    def int_closed_tag(self):
        if self.state == State.INT:
            self.current_int = self.current_int[:-1]
            self.state = State.OPENED

    def other_sym(self, char):
        if self.state == State.INT:
            self.current_int += char
        elif self.state == State.NAME:
            self.current_name += char


def main(s: str):
    return Parse().de_parse(s)
