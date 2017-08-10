#n = int(raw_input().strip())
n = 4

#for arr_i in xrange(n):
    #arr_temp = map(int,raw_input().strip().split(' '))
    #arr.append(arr_temp)
    
source = ['aba',
       'baba',
       'aba',
       'xzxb']

m = 3

search = ['aba',
          'xzxb',
          'ab']


for search_item in search:
    count = 0
    for source_item in source:
        if source_item == search_item:
            count += 1
    print str(count)
        
        


"""
There are  strings. Each string's length is no more than  characters. There are also  queries. For each query, you are given a string, and you need to find out how many times this string occurred previously. 



Input Format



The first line contains , the number of strings.
 The next  lines each contain a string.
 The nd line contains , the number of queries.
 The following  lines each contain a query string. 

Constraints

 
 
    



Sample Input


4
aba
baba
aba
xzxb
3
aba
xzxb
ab




Sample Output


2
1
0




Explanation



Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.

"""