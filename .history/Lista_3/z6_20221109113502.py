c = [i for i in range(1,11)]
a = int(input("podaj liczbę: "))
b = [i*j for i in range(1,a+1) for j in c]
print(f"\n{[i for i in b if i<=10 else '\t']}")