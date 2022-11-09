a = int(input("podaj liczbę wierszy: "))
a = int(input("podaj liczbę kolumn: "))
for i in range(1,a+1):
    for j in range(1,11):
        print(i*j, end="\t ")
    print("\n")