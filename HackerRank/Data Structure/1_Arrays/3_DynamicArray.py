
#initial_arr = map(int,raw_input().strip().split(' '))
#N = initial_arr[0]
N = 2
result = []
for i in range(N):
    result.append([]) # can not use result = [[]] * N

#arr = []
#for arr_i in xrange(initial_arr[1]):
    #arr_temp = map(int,raw_input().strip().split(' '))
    #arr.append(arr_temp)
    
arr = [ [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
      ]

lastAns = 0
for item in arr:
    if item[0] == 1:
        result[(item[1] ^ lastAns) % N].append(item[2])
    else:
        seq_index = (item[1] ^ lastAns) % N
        item_index = item[2] % len(result[seq_index])
        lastAns = result[seq_index][item_index]
        print lastAns

"""
•Create a list, , of  empty sequences, where each sequence is indexed from  to . The elements within each of the  sequences also use -indexing.
•Create an integer, , and initialize it to .
•The  types of queries that can be performed on your list of sequences () are described below: 1.Query: 1 x y 1.Find the sequence, , at index  in .
2.Append integer  to sequence .

2.Query: 2 x y 1.Find the sequence, , at index  in .
2.Find the value of element  in  (where  is the size of ) and assign it to .
3.Print the new value of  on a new line



Task 
 Given , , and  queries, execute each query.

Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia. 



Input Format



The first line contains two space-separated integers,  (the number of sequences) and  (the number of queries), respectively. 
 Each of the  subsequent lines contains a query in the format defined above.



Constraints


 •
•
•
•It is guaranteed that query type  will never query an empty sequence or index.



Output Format



For each type  query, print the updated value of  on a new line.



Sample Input


2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1




Sample Output


7
3




Explanation



Initial Values: 
 
 
 
 

Query 0: Append  to sequence . 
 
 
 

Query 1: Append  to sequence . 
 
 

Query 2: Append  to sequence . 
 
 
 

Query 3: Assign the value at index  of sequence  to , print .  
 
 
7


Query 4: Assign the value at index  of sequence  to , print .  
 
 
3

"""

