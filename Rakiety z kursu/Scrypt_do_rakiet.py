from Rakiety_z_kursu import Rockets

list_of_rockets = [Rockets() for _ in range(10)]

for rocket in list_of_rockets:
    print(rocket.id)
