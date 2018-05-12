from __future__ import division
import numpy as np
import math

"""
x         = vector in new coordinate
B         = new basis in old coordinate
Bx        = vector in old coordinate
RBx       = rotated vector in old coordinate
Binv*RBx  = rotated vector in new coordinate
"""

B = np.array([[3,1],[1,1]])     # new basis in old basis
x = np.array([1.5,0.5])         # vector in new basis

R = np.multiply(np.array([[1,-1], [1,1]]), 1/2**(1/2))     # rotation matrix
Binv = np.linalg.inv(B)                                 # B inverse

result = reduce(np.dot, (Binv, R, B, x))
print R
print result



