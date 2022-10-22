import math
a = float(input("Podaj współczynniki a: "))
b = float(input("Podaj współczynniki b: "))
c = float(input("Podaj współczynniki c: "))
a = 1

b = 5

c = 6
def pierwiastki_kw(a,b,c):
    𝛥 = pow(2,b)-(4*a*c)
    print(𝛥)
    match 𝛥 >= 0:
        case True:
            𝛥 = math.sqrt(𝛥)
            match 𝛥 > 0:
                case 0:
                    x1 = ((-b - 𝛥)/(2*a))
                    x2 = ((-b + 𝛥)/(2*a))
                    return f"𝛥 = {𝛥}, 𝑋1 = {x1}, 𝑋2 = {x2}"
                case 1:
                    x = (-b/(2*a))
                    return f"𝛥 = {𝛥}, 𝑋 = {x}"
            return 0
        case False:
            𝛥 = abs(𝛥)
            x1 = (-b / (2 * x), " + i", 𝛥) 
            x2 = (-b / (2 * x), " - i", 𝛥) 
            return "Brak pierwiastków rzeczywistych \n"
        case other:
            return "Błąd"
print(pierwiastki_kw(a,b,c))