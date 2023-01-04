import time
from functools import reduce
import matplotlib.pyplot as plt

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]
start = time.time()
print([fibonacci_of(n) for n in range(56)])
end = time.time()
print(f"czas: {end - start}\n\n")
def fibonacci_iter(n):
    a = 0
    b = 1
    while(n-2):
        c=a+b
        a,b = b,c
        print(c,end=" ")
        n=n-1
    return n
start = time.time()
print(fibonacci_iter(56))
end = time.time()
print(f"czas: {end - start}\n\n")

#plt.plot([x for x in range(10)], fib(10))
#plt.show()
