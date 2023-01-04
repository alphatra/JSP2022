import time
import random
def wstawiajaca(A):
    time_0 = time.time()
    for i in range(1, len(A)):       # w zakresie elem tablicy
        wst = A[i]              # pobiera pierwsz wartosc
        j = i - 1               # zmienna o jeden mniejsza od aktualnego indexu
        while j >= 0 and A[j] > wst:    # dopoki j jest mniejsze lub rowne 0 i tablica[j] wieksza od naszej zmiennej
            A[j + 1] = A[j]             # zamian nast elem na aktualny
            j = j - 1                   # j sie zmniejsza - przerywanie while
        A[j + 1] = wst                  # wstawia pobrany elem na miejsce
    time_w = time.time() - time_0
    return time_w

def tab(n):
    A = [random.randint(0, n) for i in range(n)]
    return A

zlicz = 0
n = 30
random.seed(1)
for i in range(n):
    zlicz += wstawiajaca(tab(100))
print("[100]Średnia: " + f'{zlicz/n}')

random.seed(1)
for i in range(n):
    zlicz += wstawiajaca(tab(100))
print("[100] Średnia2 dla tych samych: " + f'{zlicz/n}')

random.seed(2)
for i in range(n):
    zlicz += wstawiajaca(tab(200))
print("[200] Średnia: " + f'{zlicz/n}')

random.seed(2)
for i in range(n):
    zlicz += wstawiajaca(tab(200))
print("[200] Średnia2 dla tych samych: " + f'{zlicz/n}')

random.seed(3)
for i in range(n):
    zlicz += wstawiajaca(tab(300))
print("[300] Średnia: " + f'{zlicz/n}')

random.seed(3)
for i in range(n):
    zlicz += wstawiajaca(tab(300))
print("[300] Średnia2 dla tych samych: " + f'{zlicz/n}')