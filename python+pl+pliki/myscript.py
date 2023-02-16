from bankaccount import MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)


result = accountMin.try_withdraw(600)

if (result.is_ok()):
    print(result.message)
else:
    print(result.message, "tralala poszło źle")
