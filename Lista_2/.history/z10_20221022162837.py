lista = list(3*i for i in range(1,101))
print(lista)
del lista[4::3]
print(len(lista))
lista_mean = sum(lista)/len(lista)