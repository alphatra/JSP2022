from functools import reduce
def Fib(n):
    return reduce(lambda x, _ : x+[x[-1]+x[-2]],range(n-2),[0,1])
print(Fib(10))