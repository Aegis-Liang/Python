import sys


#n = int(raw_input().strip())
a = []

n = 3


#for a_i in xrange(n):
    #a_temp = map(int,raw_input().strip().split(' '))
    #a.append(a_temp)
    
a = [ [11, 2, 4],
      [4, 5, 6],
      [10, 8, -12]]    

result1 = 0
result2 = 0
for i in xrange(n):
    result1 += a[i][i]
    result2 += a[i][n-i-1]
    
print abs(result1 - result2)