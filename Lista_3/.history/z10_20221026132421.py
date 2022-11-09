lista = [list(map(int, str(i))) for i in range (100,400)]
a = [num for num in lista if num % 2 == 0]
b = [n for n in a if len(a)==3]
print(b)