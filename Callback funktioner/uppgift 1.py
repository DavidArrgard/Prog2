def addition(*val):
    summa = 0
    for arg in val:
        summa = summa + arg
    return summa


def caller(func, val):
    return func(*val)


print(caller(addition, (7, 8, 9, 5)))
