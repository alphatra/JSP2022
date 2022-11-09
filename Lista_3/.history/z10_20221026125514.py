lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [x for x in lista for i in range(0,3) if x[i]%2==0 ]
print(lista2)