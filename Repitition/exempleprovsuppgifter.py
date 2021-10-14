def chess(*x):
    if x[0] != 1:
        pass


def caller(func, x):
    return func(*x)


x = input()

print(caller(chess, x))
