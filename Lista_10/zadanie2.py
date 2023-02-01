import itertools as it
class listy():
    def __init__(self,lista):
        self.lista = lista
        self.wszystkie = []
        self.out = []
    def podlisty(self):
        for i in range(len(self.lista)+1):
            self.wszystkie.append(list(it.combinations(self.lista, i)))
        self.lista = []
        for l in self.wszystkie:
            for item in l:
                self.lista.append(list(item))
        print(self.lista)

a = [1, 2, 3]
lista = listy(a)
lista.podlisty()