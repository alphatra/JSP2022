def rgb_hsv(r,g,b):
    c_max = max(list(r,g,b))
    c_min = min(list(r,g,b))
    return c_max,c_min
try:
    my_list = []
    #Jezeli chesz zakonczyc wcisnij dowlony inny znak od liczby
    while len(my_list)<3:
        my_list.append(int(input("Dodaj liczbę do tablicy:")))
except:
    print(rgb_hsv(*my_list))