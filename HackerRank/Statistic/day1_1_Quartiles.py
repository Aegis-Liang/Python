import numpy as np

#size = int(raw_input(""))
#numbers = map(int,raw_input("").strip().split(' '))
#numbers.sort()


size = 9
numbers = [3, 7, 8, 5, 12, 14, 21, 13, 18]
numbers = np.sort(numbers)


def median(size, values):
    if size%2 == 0:
        median = (values[size/2-1]+values[size/2])/2
    else:
        median = values[size/2]
    return median 
    
if size%2 == 0: 
    low = numbers[0:size/2]
    high = numbers[size/2:size]  
else: 
    low = numbers[0:size/2]
    high = numbers[size/2+1:size]

print median(len(low), low)
print median(size, numbers)
print median(len(high), high)
