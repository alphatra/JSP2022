import random
import time


def SortWstaw(zbior):      # 1, 3, 6, 4, 2, 4, 0, 5
    for j in range(1, len(zbior)):
        i = j - 1
        while i >= 0:
            if zbior[i + 1] < zbior[i]:
                zbior[i + 1], zbior[i] = zbior[i], zbior[i + 1]
            i -= 1
    return zbior


t1 = time.time()
zbior = []
for i in range(100, 400, 100):
    for j in range(0, i):
        i = random.randint(0, 20)
        zbior.append(i)
    t2 = time.time()
    print(SortWstaw(zbior))
    print("wstawianie czas = ",t2-t1)
