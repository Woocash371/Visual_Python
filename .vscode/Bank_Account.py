class Result():

    def __init__(self, message, amount_of_money):
        self.isSucces = None
        self.message = message
        self.value = amount_of_money

    def is_ok(self):
        return self.isSucces


class Ok(Result):

    def __init__(self, message, amount_of_money):
        super().__init__(message, amount_of_money)
        self.isSucces = True


class Error(Result):

    def __init__(self, message, amount_of_money):
        super().__init__(message, amount_of_money)
        self.isSucces = False


class Account():
    """It is bank account. You can deposit here your money and take it back
    Available commands:
    Desposit, Take, Print Saldo """
    account_ID = 0

    def __init__(self, balance=0):
        self.id = Account.account_ID
        Account.account_ID += 1
        self.balance = balance

    def deposit(self, amount_of_money):
        self.balance += amount_of_money
        return Ok('Udało Ci się wpłacić środki', amount_of_money)

    def take_back(self, amount_of_money):
        if amount_of_money > self.balance:
            return Error('Nie udało Ci się wypłacić', amount_of_money)
        else:
            self.balance -= amount_of_money
            return Ok('Udało Ci się wypłacić', amount_of_money)

    def __str__(self) -> str:
        return 'Stan twojego konta wynosi: ' + str(self.balance)


class minimum_balance(Account):
    """This is a account with a minimun balance level"""

    def __init__(self, balance, minimum_balance_level):
        super().__init__(balance)
        self.minimum_balance_level = minimum_balance_level

    def __str__(self) -> str:
        return super().__str__()

    def take_back(self, amount):
        if (self.balance - amount) > self.minimum_balance_level:
            return super().take_back(amount)
        else:
            return Error('Przekroczono limit wypłaty, ', amount)
