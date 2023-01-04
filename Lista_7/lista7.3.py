import time
import random

def babelkowe(tab):
    time_0 = time.time()
    for i in range(len(tab)-1):
        j = 1
        while j < len(tab):             # poki j nie osiagnie dl tab
            if tab[j] < tab[j-1]:       # jesli tab[j] jest mniejsze od poprzedzajacego
                tmp = tab[j-1]          # poprzedzajaca w zmienna
                tab[j-1] = tab[j]       # zamiana
                tab[j] = tmp            # zamiana v2
            j += 1                      # j rosnie az przerwie while
    return time.time()-time_0

def tab(n):
    A = [random.randint(0, n) for i in range(n)]
    return A

zlicz = 0
zlicz2 = 0
n = 30
random.seed(1)
for i in range(n):
    zlicz += babelkowe(tab(100))
print("[100] Średnia: " + f'{zlicz/n}')

random.seed(1)
for i in range(n):
    zlicz += babelkowe(tab(100))
print("[100] Średnia2 dla tych samych: " + f'{zlicz2/n}')

n = 30
random.seed(2)
for i in range(n):
    zlicz += babelkowe(tab(200))
print("[200] Średnia: " + f'{zlicz/n}')

random.seed(2)
for i in range(n):
    zlicz += babelkowe(tab(200))
print("[200] Średnia2 dla tych samych: " + f'{zlicz2/n}')

n = 30
random.seed(3)
for i in range(n):
    zlicz += babelkowe(tab(300))
print("[300] Średnia: " + f'{zlicz/n}')

random.seed(3)
for i in range(n):
    zlicz += babelkowe(tab(300))
print("[300] Średnia2 dla tych samych: " + f'{zlicz2/n}')