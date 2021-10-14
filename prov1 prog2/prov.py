print("LÄMNA SPACE I MELLAN TALLEN!!!!")
x = input("Skriv in dinna nummer: ")

inputlist = x.split()

for i in range(len(inputlist)):
    inputlist[i] = int(inputlist[i])

'''print(inputlist)'''

inputlist = list(dict.fromkeys(inputlist))

'''print(inputlist)'''

for o in reversed(inputlist):
    print(o)
