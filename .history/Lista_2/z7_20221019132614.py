a = [(2,5),(1,2),(4,4)]
b = [(1,2),(4,4),(2,5)]

a = sorted(a, 
       key=lambda x: x[1])

print(a)