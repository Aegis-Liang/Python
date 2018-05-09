import numpy as np

A = np.matrix('1 2;4 5')    # it's better use nparray since matrix is only for 2D
b = np.matrix('3;6')
r = np.linalg.solve(A, b)

print r


A = np.matrix('1 2;4 5')
b = np.array([[3,6], [7,8]]).T

r = np.linalg.solve(A, b)
print r


from scipy.optimize import fsolve

def func(i):
    x, y, z = i[0], i[1], i[2]
    return [
       x + 2 * y + 3 * z - 6,
       5 * (x ** 2) + 6 * (y ** 2) + 7 * (z ** 2) - 18,
       9 * (x ** 3) + 10 * (y ** 3) + 11 * (z ** 3) - 30
   ]

r = fsolve(func,[0, 0, 0])
print r



from sympy import *
x = symbols('x')
print solve(x + 2 * (x ** 2) + 3 * (x ** 3) - 6, x)
