# One Gold Star
# Question 1-star: Stirling and Bell Numbers

# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.

# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# so S(4,2) = 7

# If instead we split the group into one group, we have just one way to 
# do it.

# 1. Dave, Sarah, Peter, Andy

# so S(4,1) = 1

# or into four groups, there is just one way to do it as well

# 1. Dave        Sarah          Peter         Andy

# so S(4,4) = 1

# If we try to split into more groups than we have people, there are no
# ways to do it.

# The formula for calculating the Stirling numbers is

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,

# B(n) is the sum of S(n,k) for k =1,2, ... , n.

# Write two procedures, stirling and bell. The first procedure, stirling 
# takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

def stirling(persons, groups):
    wholeList = makeWholeList([], persons, makeBaseList(groups))
    totalCombination = 0
    for item in wholeList:
        totalCombination += getNumberOfCombinations(item, persons)
    return totalCombination
    

def bell():
    pass


def makeBaseList(numGroups):
    distributeList = []
    for i in range(numGroups):
        distributeList.append(1)
    return distributeList


def makeWholeList(wholeList, personNumber, currentList): 
    sumOfList = 0
    isOrdered = True
    
    # compare whether each bit are in incresing order
    for k in range(len(currentList) - 1):
        if currentList[k] > currentList[k + 1]:
            isOrdered = False
            break
    
            
    if isOrdered:
        for i in currentList:
            sumOfList += i
        if sumOfList == personNumber:
            wholeList.append(currentList[:]) # [:] Clone of currentList    
        
      
    # add one to lsb
    currentList[len(currentList)-1] += 1
    for j in range(len(currentList)-1, 0, -1): # the 0 means don't do the msb check, otherwise it will be -1
        if currentList[j] > personNumber:
            currentList[j] = 1
            currentList[j-1] += 1
    
    
    
    # return if msb is larger that personNumber
    if currentList[0] > personNumber:
        return wholeList
    
    return makeWholeList(wholeList, personNumber, currentList)
    
    
def getLongestItem(singleList):
    repeatCount = 0
    repeatItem = None
    longestCount = 0
    longestItem = None
    
    for item in singleList:
        if item == repeatItem:
            repeatCount += 1
            if repeatCount > longestCount:
                longestCount = repeatCount
                longestItem = item
        else:
            repeatCount = 1
            repeatItem = item
            if repeatCount > longestCount:
                longestCount = repeatCount
                longestItem = item            
    return longestItem, longestCount        
    
    
    
def factorial(x):
    result = 1
    if x == 1:
        return result
    else:
        return x * factorial(x-1)
    
def getRepeatFactorList(singleList, result):
    if singleList == []:
        return result
    else:
        longestItem, longestCount = getLongestItem(singleList)
        removedRepeatList = []
        for item in singleList:
            if item != longestItem:
                removedRepeatList.append(item)
        result.append(longestCount)
        return getRepeatFactorList(removedRepeatList, result)
    
def c(n, m):                
    return p(n, m)/p(m, m)  # c(7, 5) = p(7, 5)/p(5, 5)

def p(n, m):
    result = 1
    for i in range(m):
        result *= n
        n = n - 1
    return result

def getNumberOfCombinations(way, person):
    
    result = 1
    for item in way:
        result = result * c(person, item)
        person = person - item
    
    factorlist = getRepeatFactorList(way, [])
    factor = 1
    for item2 in factorlist:
        factor *= factorial(item2)
        
    return result/factor


#print makeBaseList(3)
#print makeWholeList([], 7, makeBaseList(3))
#print getLongestItem([1, 1, 5])
#print factorial(3)
#print getRepeatFactorList([1, 1, 5], [])
#print getRepeatFactorList([1,1,1,2,2,2,3,3,4], [])
#print c(4, 2)
#print getNumberOfCombinations([1,1,5], 7)


print stirling(1,1)
#>>> 1
print stirling(2,1)
#>>> 1
print stirling(2,2)
#>>> 1
print stirling(2,3)
#>>>0

print stirling(3,1)
#>>> 1
print stirling(3,2)
#>>> 3
print stirling(3,3)
#>>> 1

print stirling(4,1)
#>>> 1
print stirling(4,2)
#>>> 7
print stirling(4,3)
#>>> 6
print stirling(4,4)
#>>> 1

print stirling(5,1)
#>>> 1
print stirling(5,2)
#>>> 15
print stirling(5,3)
#>>> 25
print stirling(5,4)
#>>> 10
print stirling(5,5)
#>>> 1

#print stirling(20,15) # This one could issue an error which is "RuntimeError: maximum recursion depth exceeded", don't run it
#>>> 452329200

#print bell(1)
#>>> 1
#print bell(2)
#>>> 2
#print bell(3)
#>>> 5
#print bell(4)
#>>> 15
#print bell(5)
#>>> 52
#print bell(15)
#>>> 1382958545
