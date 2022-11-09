lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [x%2 for i in range(0,len(lista)) for x in lista[i]]
print(lista2)