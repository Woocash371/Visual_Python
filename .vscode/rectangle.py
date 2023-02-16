class Rectangle():
    """Rectangle"""

    def __init__(self, width, high):
        self.width = width
        self.heigh = high

    def calculate_surface_area(self):
        return self.width * self.heigh


class Square(Rectangle):
    """Square"""

    def __init__(self, bok):
        super().__init__(bok, bok)


class Cube():

    def __init__(self, base: Square):
        self.base = base
        self.heigh = base.heigh

    def calculate_surface_area(self):
        return self.base.calculate_surface_area() * 6

    def calculate_volume(self):
        return self.base.calculate_surface_area() * self.heigh


class Cuboid():
    """docstring for Cuboid."""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_volume(self):
        return self.base.calculate_surface_area() * self.height

    def calulate_surface_area(self):
        return (self.base.calculate_surface_area() * 2) + (self.base.width * self.height * 2) + (self.base.heigh * self.height * 2)


cuboid = Cuboid(Square(2), 2)

print(cuboid.calulate_surface_area())


numbers = [1, 3, 4, 5, - 1, -2, -10000]

sum = sum([number for number in numbers if number > 0])
print(sum)
