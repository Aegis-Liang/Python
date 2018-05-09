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

import numpy as np

def projection2D(r, s):
    # r has no length, occurs error
    if(np.linalg.norm(r) == 0):
        return None
    return np.dot(r, s)/np.dot(r, r)*r


if __name__ == "__main__":
    a = np.array([1,0])
    b = np.array([5,2])
    print projection2D(a, b)