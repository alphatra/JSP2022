a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if b>a:
    Z=b%a
    Z*=Z+3
    print(Z)