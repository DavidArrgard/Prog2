x = input("Skriv din mening som ska rättas till -> ")

konosnater = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']


for y in konosnater:
    if x.count(y) > 2:
        c = x.count(y)
        res_x = x.replace(y, "", (c-2))
        print(res_x)
