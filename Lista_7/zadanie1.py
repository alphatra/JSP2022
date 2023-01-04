import time


# n = int(input("Podaj ile wyrazów wypisać "))
def fibboo(n):
    wyr0 = 0
    wyr1 = 1
    for i in range(0, n + 1):
        print(wyr0)
        wyr0, wyr1 = wyr1, wyr1 + wyr0


def fib(n):  #rekurencyjnie
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


t1 = time.time()
n = 100
fibboo(n)
t2 = time.time()
print("czas= ", t2 - t1)

# niżej rekurencyjnie

t1 = time.time()
# n = int(input("Podaj ile wyrazów wypisać "))
n = 19
for i in range(0, n+1):
    print(fib(i))
t2 = time.time()
print("czas2= ", t2-t1)
