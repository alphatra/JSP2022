lista = list(3*i for i in range(1,101))
print(lista)
del lista[4::3]
print(lista)
lista_mean = sum(lista)/len(lista)
print(lista_mean)