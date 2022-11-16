try:
    my_list = []
    #Jezeli chesz zakonczyc wcisnij dowlony inny znak od liczby
    while len(my_list)<3:
        my_list.append(int(input("Dodaj liczbę do tablicy:")))
except:
    print(my_list)