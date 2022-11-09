lista = [list(map(int, str(i))) for i in range (100,400)]
for x in lista:
    a = list(filter(lambda x: (x % 2 != 0), lista))
    print(x)