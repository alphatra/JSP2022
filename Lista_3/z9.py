a = int(input("podaj liczbę wierszy: "))
b = int(input("podaj liczbę kolumn: "))
x=[]
for i in range(1,a+1):
    for j in range(1,b+1):
        x.append([i*j])
        print(i*j, end="\t ")
    print("\n")
print(x)