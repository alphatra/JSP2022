import math
a = int(input("Podaj współczynniki a: "))
b = int(input("Podaj współczynniki b: "))
c = int(input("Podaj współczynniki c: "))
def pierwiastki_kw(a,b,c):
    𝛥 = (b**2)-(4*a*c)
    match 𝛥 != 0:
        case True:
            𝛥 = math.sqrt(𝛥)
            x1 = (-b - 𝛥)/(2*a)
            x2 = (-b + 𝛥)/(2*a)
            return f"𝛥 = {𝛥}, 𝑋1 = {x1}, 𝑋2 = {x2}"
        case False:
            x = -b/(2*a)
            return f"𝛥 = {𝛥}, 𝑋 = {x}"
print(pierwiastki_kw(a,b,c))