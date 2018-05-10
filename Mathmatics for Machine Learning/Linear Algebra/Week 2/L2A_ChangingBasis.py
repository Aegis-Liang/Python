"""
The basic idea of this lecture is to do the project to the x,y coordinate of the new basis,
There is other way to do this job.

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

so |s|cos(theta) is the length of s to r with original basis, to change to the length with new basis, divide it by |r|,
so it's (r.s)/|r|^2
"""

from __future__ import division
import numpy as np

def projection2Basis(r, s):
    # r has no length, occurs error
    if(np.linalg.norm(r) == 0):
        return None
    return np.dot(r, s)/(np.linalg.norm(r)**2)

if __name__ == "__main__":
    a = np.array([3,4])
    b1 = np.array([2,1])
    b2 = np.array([-2,4])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)
    
    # 1
    a = np.array([5,-1])
    b1 = np.array([1,1])
    b2 = np.array([1,-1])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)    
    
    # 2
    a = np.array([10,-5])
    b1 = np.array([3,4])
    b2 = np.array([4,-3])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)        
    
    # 3
    a = np.array([2,2])
    b1 = np.array([-3,1])
    b2 = np.array([1,3])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)     
    
    # 4
    a = np.array([1,1,1])
    b1 = np.array([2,1,0])
    b2 = np.array([1,-2,-1])
    b3 = np.array([-1,2,-5])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)
    print projection2Basis(b3, a) 
    
    # 5
    a = np.array([1,1,2,3])
    b1 = np.array([1,0,0,0])
    b2 = np.array([0,2,-1,0])
    b3 = np.array([0,1,2,0])
    b4 = np.array([0,0,0,3])
    
    print projection2Basis(b1, a)
    print projection2Basis(b2, a)
    print projection2Basis(b3, a)  
    print projection2Basis(b4, a)   