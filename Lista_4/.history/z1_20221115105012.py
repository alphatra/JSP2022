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
    a = input(" - działanie: ")
    if(a==0):
        print(sum(my_list))
    else:
        print(iloczyn(my_list))
