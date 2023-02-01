import numpy
wsp = numpy.array([[1, 2, 3, -2, -1], [3, 5, 5, -3, -9], [2, 3, 2, 0, -8], [2, 6, 7, -5, 1], [1, 2, 6, -4, -10]])
liczby = numpy.array([6, 2, -5, 17, 12])

wyniki = numpy.linalg.solve(wsp, liczby)
print("x = ", wyniki[0], " y = ", wyniki[1], " z = ", wyniki[2], " t = ", wyniki[3], " u = ", wyniki[4])