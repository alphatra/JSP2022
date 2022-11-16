a = int(input("podaj liczbę wierszy: "))
b = int(input("podaj liczbę kolumn: "))
for i in range(1,a+1):
    for j in range(1,b+1):
        x.append([i*j])
print(x for x in range(1,a+1))