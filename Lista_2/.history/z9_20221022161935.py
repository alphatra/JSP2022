from itertools import chain
from re import L
lista = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
result = list(chain.from_iterable(lista))
print(result)