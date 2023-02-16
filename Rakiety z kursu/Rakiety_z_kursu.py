from random import randint
from math import sqrt


class Rockets():
    rocket_id = 0

    def __init__(self, speed=1, horizontal_position=0, altitude=0):
        self.id = Rockets.rocket_id
        Rockets.rocket_id += 1
        self.altitude = altitude
        self.speed = speed
        self.horizontal_position = horizontal_position

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        # Mówi o tym co będzie wypisywać obiekt
        return ('Wysokość rakiety to: ' + str(self.altitude) +
                '\nSzybkość rakiety: ' + str(self.speed) +
                "\nPozycja w poziome: " + str(self.horizontal_position))


class rocketBoard():
    """To jest tablica rakiet, jako argument podaj ilość rakiet"""

    def __init__(self, amountOfRocket=1):

        self.rockets = [Rockets(randint(1, 10)) for _ in range(amountOfRocket)]

        for _ in range(10):
            chosen_rocket = randint(0, len(self.rockets) - 1)
            self.rockets[chosen_rocket].moveUp()

        for element in self.rockets:
            print(element)

    def __getitem__(self, key):
        # Fukcja getitem robi obiekt indeksowalnym
        return self.rockets[key]

    def __setitem__(self, key, value):
        # Pozwala przypisać do danego obiektu w planszy wartość
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1: Rockets, rocket2: Rockets) -> float:
        multiply_y_distance = (rocket2.altitude - rocket1.altitude) ** 2
        multiply_x_distance = (
            rocket2.horizontal_position - rocket1.horizontal_position) ** 2
        return sqrt(multiply_x_distance + multiply_y_distance)

    def get_amount_of_rockets(self):
        return len(self.rockets)

    def __len__(self):
        return self.get_amount_of_rockets()
