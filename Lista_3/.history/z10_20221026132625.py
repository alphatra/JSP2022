lista = [list(map(int, str(i))) for i in range (100,400)]
x=[]
for x in lista:
    a = [num for num in x if num % 2 == 0]
    b = [n for n in a if len(a)==3]
    x+=b

print(x)