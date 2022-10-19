from cmath import sin
import math
print("Podaj bok a: ")
a=input()
print("Podaj bok b: ")
b=input()
print("Podaj bok c: ")
kat=input()
pole = a*b*sin(math.sin(kat*math.pi/180))*1/2
print("Pole: ", pole)