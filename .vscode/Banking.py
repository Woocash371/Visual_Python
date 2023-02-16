from Bank_Account import Account
konto = Account()

wplata = konto.deposit(100)
wyplata = konto.take_back(200)


print(wplata.message)
print(wyplata.message)
