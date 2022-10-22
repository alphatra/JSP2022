import math

a = int(input("Podaj współczynniki a: "))
b = int(input("Podaj współczynniki b: "))
c = int(input("Podaj współczynniki c: "))
def pierwiastki_kw(a,b,c):
    𝛥 = math.sqrt(((b**2)-(4*a*c)))
    match 𝛥 >= 0:
        case True:
            match 𝛥 > 0:
                case 0:
                    x1 = (-b - 𝛥)/(2*a)
                    x2 = (-b + 𝛥)/(2*a)
                    return f"𝛥 = {𝛥}, 𝑋1 = {x1}, 𝑋2 = {x2}"
                case 1:
                    x = -b/(2*a)
                    return f"𝛥 = {𝛥}, 𝑋 = {x}"
            return 0
        case False:
            return "Brak pierwiastków"
        case other:
            return "Błąd"
print(pierwiastki_kw(a,b,c))