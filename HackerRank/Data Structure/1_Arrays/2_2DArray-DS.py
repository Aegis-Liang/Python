#arr = []
#for arr_i in xrange(6):
    #arr_temp = map(int,raw_input().strip().split(' '))
    #arr.append(arr_temp)
    
arr = [ [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
      ]

def calculate(arr, row, col):
    result = 0
    result += arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] + arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]
    return result

def find_max(arr):
    max_result = -100 # fail 2 test cases if set to 0
    for i in range(0, 4):
        for j in range(0, 4):
            current = calculate(arr, i, j)
            if current > max_result:
                max_result = current
    return max_result

print find_max(arr)

"""
Context 
 Given a  2D Array, : 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g


There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. 

Task 
 Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.



Input Format



There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .



Constraints


 • 
•



Output Format



Print the largest (maximum) hourglass sum found in .



Sample Input


1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0




Sample Output


19




Explanation



 contains the following hourglasses:
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0


The hourglass with the maximum sum () is:
2 4 4
  2
1 2 4
"""
                