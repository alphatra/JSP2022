from cmath import phase
import math

z = complex(input())
print("Modul: ",abs(z),"Argument", math.phase(z)*(math.pi/180))