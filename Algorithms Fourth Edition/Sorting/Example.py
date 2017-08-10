def sort(a):
    pass

def less(v, w):
    if "__cmp__" in dir(v):
        return v.__cmp__(w) == -1
    elif "__lt__" in dir(v):
        return v.__lt__(w)
    else:
        return None

def exch(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
        

def show(a):
    for i in a:
        print str(i),
    print ""

def isSorted(a):
    for i in xrange(1, len(a)):
        if (less(a[i], a[i-1])):
            return False
    return True


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    show(arr)
    print isSorted(arr)
    exch(arr, 0, 1)
    print arr   
    print isSorted(arr)

    arr = list("SORTEXAMPLE")
    show(arr)    
    print isSorted(arr)
    exch(arr, 0, 1)
    print arr
    print isSorted(arr)
    
    
    print less(1, 2)
    print less("a", "b")    
    