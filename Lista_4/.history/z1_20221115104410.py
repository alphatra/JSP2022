from functools import reduce
def suma(n):
    return sum(n)
def iloczyn(n):
    return reduce(lambda a,b: a*b, n)
try:
    my_list = []
    #Jezeli chesz zakonczyc wcisnij dowlony inny znak od liczby
    while True:
        my_list.append(int(input("Dodaj liczbę do tablicy:")))

except:
    print(my_list)
    print("Wybierz działanie: 0 - dodawnie \t 1 - iloczyn")
    a = bool(input(" - działanie: "))
    match a:
        case 0:
            print(a(my_list))
        case 1:
            print(iloczyn(my_list))
