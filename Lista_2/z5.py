a=input("pierwszy wyraz")
b=input("drugi wyraz")
c= a[:int(len(a)/2)]+b+a[int(len(a)/2):]
print(c)