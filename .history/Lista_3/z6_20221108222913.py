j = [i for i in range(1,11)]
a = int(input("podaj liczbę: "))
print(f"{j}\n{[(lambda x: x + 1)(j)]}")