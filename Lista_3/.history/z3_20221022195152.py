import math
a = float(input("Podaj współczynniki a: "))
b = float(input("Podaj współczynniki b: "))
c = float(input("Podaj współczynniki c: "))
a = 1

b = 5

c = 6
def pierwiastki_kw(a,b,c):
    delta = pow(b,2)-4*a*c
    print(delta)
    match delta >= 0:
        case True:
            delta = math.sqrt(delta)
            match delta > 0:
                case 0:
                    x1 = ((-b - delta)/(2*a))
                    x2 = ((-b + delta)/(2*a))
                    return f"delta = {delta}, 𝑋1 = {x1}, 𝑋2 = {x2}"
                case 1:
                    x = (-b/(2*a))
                    return f"delta = {delta}, 𝑋 = {x}"
            return 0
        case False:
            delta = abs(delta)
            x1 = (-b / (2 * x), " + i", delta) 
            x2 = (-b / (2 * x), " - i", delta) 
            return "Brak pierwiastków rzeczywistych \n"
        case other:
            return "Błąd"
print(pierwiastki_kw(a,b,c))