
class Square:
    def __init__(self, name, leg_length):
        self.name   = name
        self.sides  = 4
        self.length = leg_length
        self.goingShopping = None

    def set_state(self, state):
        self.goingShopping = state

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def get_area(self):
        #A = self.length * self.length
        A = self.length**2
        return A

    def get_sides(self):
        return self.sides


class Triangle:
    def __init__(self, name, b_length, h_length):
        self.name   = name
        self.sides  = 3
        self.base   = b_length
        self.height = h_length
        self.goingShopping = None

    def set_state(self, state):
        self.goingShopping = state

    def set_name(self, new_name):
        self.name = new_name

    def get_area(self):
        A = 0.5 * self.base * self.height
        return A
    