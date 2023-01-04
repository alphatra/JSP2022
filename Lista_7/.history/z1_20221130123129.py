import time
from functools import reduce
import matplotlib.pyplot as plt

def fib_Rek(n):
    if (n==1 and n==2):
        return 1
    else:
        return(fib_Rek(n-1)+fib_Rek(n-2))
start = time.time()
print(f"x -> 10 fibonacci(x=10):{fib_Rek(10)}")
end = time.time()
print(end - start)
#plt.plot([x for x in range(10)], fib(10))
#plt.show()
