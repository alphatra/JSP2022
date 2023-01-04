lista_wielo = [2*x for x in range(1,50)]
def check(x):
    if x%3==0:
        return 'Syk'
    if x%5==0:
        return 'Bzyk'
    if x%3 == 0 and x%5 == 0:
        return 'SykBzyk'
    return x
for x in lista_wielo:
    print(check(x))