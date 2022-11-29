from math import log
def harmonicSum(n):
    sequance = [1/z for z in range(1,n+1)]
    return sum(sequance)
print(harmonicSum(100000))
print(log(100000))