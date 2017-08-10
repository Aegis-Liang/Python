import math

#x1,v1,x2,v2 = raw_input().strip().split(' ')
#x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

x1,v1,x2,v2  = [0, 3, 4, 2]

if v1 == v2:
    if x1 == x2:
        print "YES"
    else:
        print "NO"
else:
    n = (x2 - x1)/float(v1 - v2)
    if n == math.ceil(n) and n >= 0:
        print "YES"
    else:
        print "NO"


