import pandas as pd
a = {"Łukasz": 13, "Diana": 10, 'Ada': 10, }

print(pd.Series(a))


print('Show')
print('Czy Python już działa?')


def nowa_funckja(x):
    if x < 5:
        print('x jest mniejszy od 5')
    else:
        print('x nie jest mniejszy od 5')


nowa_funckja(234)
a = 0
lista = []
while a < 10:
    lista.append(a)
    a = a + 1
