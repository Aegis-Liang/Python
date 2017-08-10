import numpy as np
import math

#size = int(raw_input())
#X = map(float,raw_input().strip().split(' '))

size = 5
X = [10, 40, 30, 50, 20]

u = np.mean(X)


print "%0.1f" % math.sqrt(np.mean(map(lambda x:(x-u)**2, X)))



"""
import math

size = int(raw_input())
X = map(float,raw_input().strip().split(' '))

def mean(arr):
    return sum(arr)/len(arr)

u = mean(X)


print "%0.1f" % math.sqrt(mean(map(lambda x:(x-u)**2, X)))
"""