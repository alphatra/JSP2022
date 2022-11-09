lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [i for i in range(0,3) for x in lista]
print(lista2)