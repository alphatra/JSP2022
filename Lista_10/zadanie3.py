import itertools as it
class listy():
    def __init__(self,lista):
        self.lista = lista
        self.wszystkie = []
        self.out = []
    def podlisty(self):
        self.wszystkie.append(list(it.combinations(self.lista, 3)))
        self.lista = []
        for l in self.wszystkie:
            for item in l:
                self.lista.append(list(item))
        self.wszystkie = []
        for i in self.lista:
            if i[0]+i[1]+i[2] == 0:
                self.wszystkie.append(i)
        return self.wszystkie

a = [1, 2, -3, 3, 4, 7, -7]
lista = listy(a)
print(lista.podlisty())