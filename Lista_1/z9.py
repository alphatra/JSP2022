from cmath import phase
import cmath

z = complex(input("Podaj liczbę zespoloną"))
print("Modul: ",abs(z),"Argument", cmath.phase(z))