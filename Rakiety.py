import random


class Rocket():
    def __init__(self):
        self.high = 0
        self.velocity = 0
        self.time = 0

    def set_velocity_of_rocket(self):
        self.velocity = random.randrange(0, 10000, 1)

    def set_time_of_fly(self):
        self.time = random.randrange(0, 60, 1)

    def calculation_high_of_fly(self):
        self.high += self.time * self.velocity


list_of_rocket = [Rocket() for _ in range(6)]
x = 0


while x < 10:
    x += 1
    chosen_rocket_index = random.randint(0, 5)
    list_of_rocket[chosen_rocket_index].set_time_of_fly()
    list_of_rocket[chosen_rocket_index].set_velocity_of_rocket()
    list_of_rocket[chosen_rocket_index].calculation_high_of_fly()


for element in list_of_rocket:
    index = list_of_rocket.index(element)
    print('Rocket', index, element.high, '[m]')
