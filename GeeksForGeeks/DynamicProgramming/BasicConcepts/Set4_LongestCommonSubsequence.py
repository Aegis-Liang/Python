
"""
1) L("GGTAB" "XTXAYB") = 1 + L("GGTA" XTXAY")
2) L("BCDGH" "EDFHR") = MAX ( L("BCDG" "EDFHR", L("BCDGH" "EDFH") )
"""
# A Naive recursive Python implementation of LCS problem

def lcs1(X, Y, m, n):

    if m == 0 or n == 0:
        return 0;
    elif X[m-1] == Y[n-1]:
        return 1 + lcs1(X, Y, m-1, n-1);
    else:
        return max(lcs1(X, Y, m, n-1), lcs1(X, Y, m-1, n));


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs1(X , Y, len(X), len(Y))



"""
LCS    EMPTY    A    G    G    T    A    B
EMPTY      0    0    0    0    0    0    0
                | ^\   ^\      |
G          0 -- 0    1    1 -- 1    1    1

X          0    0    1    1    1    1    1

T          0    0    1    1    2    2    2

X          0    0    1    1    2    2    2

A          0    1    1    1    2    3    3

Y          0    1    1    1    2    3    3

B          0    1    1    1    2    3    4

if two letters are not the same, get the larger value from the its left and top.
if two letters are the same, add one from its top left value. (It seems that top is OK, left is not OK)

"""

# Dynamic Programming implementation of LCS problem

def lcs(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
#end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)