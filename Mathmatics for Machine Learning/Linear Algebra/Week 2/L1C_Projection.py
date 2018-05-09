"""
c^2 = (r-s)^2 = r^2 -2rs + s^2 = r^2 + s^2 -2|r||s|cos(theta)
r.s = |r||s|cos(theta)  ==>  |s|cos(theta) = (r.s)/|r|


   s
    /
   /
  /
 /
/   theta
-----------
|    |     r
<-x ->

(scalar projection)              |x| = |s|cos(theta) = (r.s)/|r|   
unit vector with direction r     r/|r|
(vector projection)              x = |x|*(r/|r|) = ((r.s)/|r|)/(r/|r|) = (r.s)*r/(|r||r|) = r*((r.s)/(r.r))

"""
from __future__ import division     # this must be imported in python 2, otherwise int/int = int not float
import numpy as np

# project s to r, it seems work for all dimension, remove the 2D from the function name
def projection(r, s):
    # r has no length, occurs error
    if(np.linalg.norm(r) == 0):
        return None
    return np.dot(r, s)/np.dot(r, r)*r


if __name__ == "__main__":
    a = np.array([1,0])
    b = np.array([5,2])
    print projection(a, b)
    
    c = np.array([3,-4,0])
    d = np.array([10,5,-6])
    print projection(c, d)