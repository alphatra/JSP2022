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

[fibonacci_of(n) for n in range(15)]
start = time.time()
[fibonacci_of(n) for n in range(15)]
end = time.time()
print(end - start)
#plt.plot([x for x in range(10)], fib(10))
#plt.show()
