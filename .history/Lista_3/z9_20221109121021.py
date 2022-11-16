a = int(input("podaj liczbę wierszy: "))
b = int(input("podaj liczbę kolumn: "))
print([[x*j for j in range(1,b+1)] for x in range(1,a+1) ])