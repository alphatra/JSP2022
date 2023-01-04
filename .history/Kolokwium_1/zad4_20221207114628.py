lista_wielo = [2*x for x in range(1,50)]
def check(x):
    if x%3==True:
        return 'Syk'
    if x%5==True:
        return 'Bzyk'
    if x%3 == True and x%5 == True:
        return 'SykBzyk'
    return x
for x in lista_wielo:
    print(check(x))