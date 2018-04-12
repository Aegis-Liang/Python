"""
Recursion tree for execution of fib(5)

                              
                         fib(5)
                     /             \
               fib(4)                fib(3)
             /      \                /     \
         fib(3)      fib(2)         fib(2)    fib(1)
        /     \        /    \       /    \
  fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
  /    \
fib(1) fib(0)
"""


"""
a) Memoization (Top Down): The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions. We initialize a lookup array with all initial values as NIL. Whenever we need solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise we calculate the value and put the result in lookup table so that it can be reused later.

Following is the memoized version for nth Fibonacci Number.
"""
# Python program for Memoized version of nth Fibonacci number

# Function to calculate nth Fibonacci number
def fib1(n, lookup):

    # Base case
    if n == 0 or n == 1 :
        lookup[n] = n

    # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib1(n-1 , lookup)  + fib1(n-2 , lookup) 

    # return the value corresponding to that value of n
    return lookup[n]
# end of function

# Driver program to test the above function
def main1():
    n = 300
    # Declaration of lookup table
    # Handles till n = 100 
    lookup = [None]*(n+1)
    print "Fibonacci Number is ", fib1(n, lookup)

    
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


"""
b) Tabulation (Bottom Up): The tabulated program for a given problem builds a table in bottom up fashion and returns the last entry from table. For example, for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2) then fib(3) and so on. So literally, we are building the solutions of subproblems bottom-up.

Following is the tabulated version for nth Fibonacci Number.
"""

# Python program Tabulated (bottom up) version
def fib2(n):

    # array declaration
    f = [0]*(n+1)

    # base case assignment
    f[1] = 1

    # calculating the fibonacci and storing the values
    for i in xrange(2 , n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# Driver program to test the above function
def main2():
    n = 300
    print "Fibonacci number is " , fib2(n)

if __name__=="__main__":
    main1()    
    main2()

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)