lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [z for x in lista for i in range(0,3) for z in x[i]]
print(lista2)