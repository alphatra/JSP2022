lista = [list(map(int, str(i))) for i in range (100,400)]
for x in lista:
    a = [num for num in x if num % 2 == 1]
    print(a)