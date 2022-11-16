from math import pi
def degrad(val,type):
    match type:
        case 0:
            return val*(180/pi)
        case 1:
            return val*(pi/180)
print(degrad(90,1))