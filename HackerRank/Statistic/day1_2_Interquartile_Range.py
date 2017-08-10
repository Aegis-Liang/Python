

#size = int(raw_input(""))
#X = map(float,raw_input("").strip().split(' '))
#F = map(int,raw_input("").strip().split(' '))

size = 6
X = [6, 12, 8, 10, 20, 16]
F = [5, 4, 3, 2, 1, 5]


def median(size, values):
    if size%2 == 0:
        median = (values[size/2-1]+values[size/2])/2
    else:
        median = values[size/2]
    return median 

arr = []
for i in range(size):
    arr.extend([X[i]] * F[i])
    
    
arr.sort()

if len(arr)%2 == 0: 
    low = arr[0:len(arr)/2]
    high = arr[len(arr)/2:len(arr)]  
else: 
    low = arr[0:len(arr)/2]
    high = arr[len(arr)/2+1:len(arr)]

Q1 = median(len(low), low)
Q2 = median(len(X), X)
Q3 = median(len(high), high)


print Q3 - Q1
