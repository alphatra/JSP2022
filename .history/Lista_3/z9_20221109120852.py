a = int(input("podaj liczbę wierszy: "))
b = int(input("podaj liczbę kolumn: "))
z=[]
for i in range(1,a+1):
    for j in range(1,b+1):
        z.append([i*j])
print([[x*j for j in range(1,b+1)] for x in range(1,a+1) ])