a = int(input("podaj liczbę: "))
for i in range(1,a+1):
    for j in range(1,11):
        print(i*j, sep=" ", end="")
    print("\n")