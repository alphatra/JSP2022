import numpy as n
import matplotlib.pyplot as plt
v0 = float(input("Podaj predkosc poczatkowa [m/s]: "))
alpha = float(input("Podaj kat rzutu [stopnie]: ")) * n.pi / 180
tc = 2 * v0 * n.sin(alpha) / 9.81
zasieg = 2 * v0**2 * n.sin(alpha)**2 / 9.81
hmax = v0**2 * n.sin(alpha)**2 / (2 * 9.81)

print("czas lotu = ", tc, "  zasieg = ", zasieg, "  wysokosc max = ", hmax)

freq = 100           # im wiecej tym wieksza dokladnosc
t = n.linspace(0, tc, freq)
vx = [v0 * n.cos(alpha) for i in range(freq)]
vy = v0 * n.sin(alpha) - 9.81 * t
x = vx * t
y = v0 * t * n.sin(alpha) - 9.81 * t * t / 2

plt.subplot(221, title="Prędkości", xlabel="t[s]", ylabel="v[m/s]")
plt.plot(t, vx, t, vy)
plt.legend(['vx(t)', 'vy(t)'])

plt.subplot(222, title="Położenie", xlabel="t[s]", ylabel="x [m] / y [m]")
plt.plot(t, x, t, y)
plt.legend(['x(t)', 'y(t)'])

plt.subplot(223, title="Tor ruchu", xlabel="x[m]", ylabel="y[m]")
plt.plot(x, y)
plt.legend('y(x)')
plt.subplots_adjust(hspace=1)
plt.show()