lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [x[i] for x in lista for i in range(0,3)]
print(lista2)