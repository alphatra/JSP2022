import time

# lst = []
def fib_r(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_r(n - 1) + fib_r(n - 2)

def fib_i(n):
    a, b = 0, 1             # pierwsze dwa
    for i in range(0, n):   # w zakresie n
        a, b = b, a + b     # do a
    return a

n = int(input("Podaj n: "))
time_0 = time.time()
for i in range(0, n):
    print(fib_r(i), end=" ")
print(time.time() - time_0, end="\n\n")

time_0 = time.time()
for i in range(0, n):
    print(fib_i(i), end=" ")
print(time.time() - time_0)
