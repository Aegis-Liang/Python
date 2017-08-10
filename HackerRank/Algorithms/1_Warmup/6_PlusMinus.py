import sys


#n = int(raw_input().strip())
#arr = map(int,raw_input().strip().split(' '))

n = 6
arr = [-4, 3, -9, 0, 4, 1] 
print len([x for x in arr if x > 0])/float(n)
print len([x for x in arr if x < 0])/float(n)
print len([x for x in arr if x == 0])/float(n)