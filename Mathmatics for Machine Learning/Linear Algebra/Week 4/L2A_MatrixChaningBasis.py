import numpy as np

A = np.array([[3,1],[1,1]])     # new basis in old basis
b = np.array([1.5,0.5])         # vector in new basis

c = A.dot(b)                    # vector in old basis
print c


Ainv = np.linalg.inv(A)         # A inverse 
d = Ainv.dot(c)                 # get back b, vector in new basis
print d