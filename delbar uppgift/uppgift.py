for i in range(1000):
    if i % 7 == 0 or 7 in divmod(i, 1000):
        print(i)
