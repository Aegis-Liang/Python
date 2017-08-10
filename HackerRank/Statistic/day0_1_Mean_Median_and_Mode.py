import numpy as np
from scipy import stats

#size = int(raw_input(""))
#numbers = map(int,raw_input("").strip().split(' '))

size = 5
numbers = [1, 1, 1, 2, 3]

print(np.average(numbers))
print(np.median(numbers))
print(stats.mode(numbers)[0][0])