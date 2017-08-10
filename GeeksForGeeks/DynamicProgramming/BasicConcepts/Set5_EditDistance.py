"""recursive solution:
"""

def editDistance(str1, str2, m , n):
    if m == 0:
        return n
    
    if n == 0:
        return m
    
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    else:
        return 1 + min(editDistance(str1, str2, m, n-1),         # Insert
                       editDistance(str1, str2, m-1, n),         # Remove
                       editDistance(str1, str2, m-1, n-1)        # Replace
        )
    
    
    
"""
LCS    EMPTY    M    A    R    C    H
EMPTY      0    1    2    3    4    5    
                            ^\
C          1    1    2    3    3    4    
                  ^\
A          2    2    1    2    3    4    
                       ^\
R          3    3    2    1    2    3    

T          4    4    3    2    2    3    

"""

def editDistDP(str1, str2, m, n):
    dp = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
    
    for i in xrange(m+1):
        for j in xrange(n+1):
            
            if i == 0:
                dp[i][j] = j
            
            elif j == 0:
                dp[i][j] = i
            
            elif str1[i-1] == str2[j-1]:                     # we use i and j here, not use m and n, one more row and column that m and n
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                
    return dp[m][n]
    


    
if __name__=="__main__":
    str1 = "sunday"
    str2 = "saturday"
    print str(editDistance(str1, str2, len(str1), len(str2)))
    print str(editDistDP(str1, str2, len(str1), len(str2)))