c = [i for i in range(1,11)]
a = int(input("podaj liczbę: "))
b = [i*j for i in range(1,a+1) for j in c]
print(f"\n{[i if i <=10 else 'a\t' for i in b]}")