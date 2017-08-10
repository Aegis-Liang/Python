
#setup_arr = map(int,raw_input().strip().split(' '))
setup_arr = [5, 3]
m = setup_arr[0]
n = setup_arr[1]

result = [0] * m
arr = []

#for arr_i in xrange(n):
    #arr_temp = map(int,raw_input().strip().split(' '))
    #arr.append(arr_temp)
    
""" different matrix
  0    0    0     0  0 
  100  0    -100  0  0     <--- 1 2 100, 3rd col is 100 less than 2nd col 
  100  100  -100  0  0     <--- 2 5 100, 2nd col is 100 more than 1st col
  100  100  0     0  -100  <--- 3 4 100, now 3rd is equal to 2nd, and 5th is 100 less than 4th col
"""
    
arr = [[1, 2, 100],
       [2, 5, 100],
       [3, 4, 100]]

#zeros = [0] * m                                # Test case 5 don't pass!!!
#for item in arr:
    #be_add = zeros[0:item[0]-1] + [item[2]] * (item[1] - item[0] + 1) + zeros[item[1]:]
    #result = map(int.__add__, result, be_add)
    
for item in arr:
    result[item[0]-1] += item[2]
    if item[1] < m:
        result[item[1]] -= item[2]
  
max_result = 0
current_result = 0
for i in range(m):
    current_result += result[i]
    max_result = max(max_result, current_result)
    
#for i in range(1, m):                          # Test Case 7 don't pass!!!
    #result[i] = result[i] + result[i-1]
#print max(result)
    
    
print max_result



"""You are given a list of size , initialized with zeroes. You have to perform  operations on the list and output the maximum of final values of all the  elements in the list. For every operation, you are given three integers ,  and  and you have to add value  to all the elements ranging from index  to (both inclusive). 



Input Format



First line will contain two integers  and  separated by a single space.
    Next  lines will contain three integers ,  and  separated by a single space.
    Numbers in list are numbered from  to . 



Constraints











Output Format



A single line containing maximum value in the updated list.



Sample Input


5 3
1 2 100
2 5 100
3 4 100




Sample Output


200




Explanation



After first update list will be 100 100 0 0 0. 
    After second update list will be 100 200 100 100 100.
    After third update list will be 100 200 200 200 100.
    So the required answer will be 200.
"""