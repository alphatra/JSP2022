lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [i[x] for i in len(lista) for x in i]
print(lista2)