typ = ["parzysta","nieparzysta"]
liczba = int(input("podaj literę do sprawdzenia: "))

print("liczba jest parzysta" if liczba % 2 == 0 else "liczba jest nieparzysta")
print("%s",typ[liczba%2])