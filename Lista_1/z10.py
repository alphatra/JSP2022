import cmath

z=1j

x = cmath.sin(z)
y = cmath.cos(z)

print(x.real,x.imag)
print(y.real,y.imag)
print(x**2+y**2,x**2+y**2==1)