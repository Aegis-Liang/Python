"""
vector r
r^2 = r1^2 + r2^2 = |r|^2
cosine rule: c^2 = a^2 + b^2 - 2|a||b|cos(theta)

c = r-s
c^2 = (r-s)^2 = r^2 -2rs + s^2 = r^2 + s^2 -2|r||s|cos(theta)
rs = |r||s|cos(theta)

if cos(theta) = 0, then rs = 0

"""

import numpy as np

a = np.array([1,0])
b = np.array([0,1])
print np.dot(a, b)