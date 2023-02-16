"""class Serniki:
    rodzynki = False
    krem = 'brak'

    def dodaj_rodzynki(self, sypanie):
        self.rodzynki = sypanie

    def polej_kremem(self, polewa):
        self.krem = polewa


sernik1 = Serniki()


print('sernik1.rodzynki: ', sernik1.rodzynki)

sernik1.dodaj_rodzynki(True)


print('sernik1.rodzynki: ', sernik1.rodzynki)


sernik2 = Serniki()

sernik2.polej_kremem('Sernik został polany kremem')


sernik2.krem
print('sernik2.krem: ', sernik2.krem)

"""



class Jablecznik():
    def __init__(self, ciasto, rodzaj_jablek):
        self.ciasto = ciasto
        self.rodzaj_jablek = rodzaj_jablek


Jablecznik1 = Jablecznik('Drozdzowe', 'Jonagoldy')
Jablecznik1.rodzaj_jablek += ' Szara Reneta'

print(Jablecznik1.rodzaj_jablek)
