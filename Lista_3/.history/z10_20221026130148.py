lista = [list(map(int, str(i))) for i in range (100,400)]
lista2 = [lambda z:z[i]%2==0,x for x in lista for i in range(0,3)]
print(lista2)