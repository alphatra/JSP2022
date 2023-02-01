import math

class Koło():
    def __init__(self, r):
        self.r = r
    def pole(self):
        print("Pole koła = ", math.pi * self.r ** 2)
    def obwod(self):
        print("Pole koła = ", 2 * math.pi * self.r)


kolo = Koło(5)
kolo.pole()