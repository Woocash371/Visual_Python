class square():
    """This class is about square"""

    def __init__(self, a):
        self.a = a
        self.area = 'Uncount'

    def calculate_fig_area(self):
        self.area = self.a * self.a
        return self.area


class rectangle(square):
    """Rectangle"""

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def calulate_fig_area(self):
        self.area = self.a * self.b
        return self.area


class Cube(square):
    """This is class about Cubes"""

    def __init__(self, a):
        super().__init__(a)

    def calculate_Cube_base(self):
        return super().calculate_fig_area()

    def calculate_Cube_Volume(self):
        return super().calculate_fig_area() * self.a


szescian = Cube(7)
print(szescian.calculate_Cube_base())
print(szescian.calculate_Cube_Volume())
