c = [i for i in range(1,11)]
a = int(input("podaj liczbę: "))
b = [i*j for i in range(1,a+1) for j in c]
for i in b:
    if(i%2):
        print("/n")
    print(i)