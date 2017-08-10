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

def compareTo(v, w):
    if "__cmp__" in dir(v):
        return v.__cmp__(w)
    elif "__lt__" in dir(v):
        if v.__lt__(w):
            return -1
        elif v.__eq__(w):
            return 0
        else:
            return 1
    else:
        return None
        


class Selection(object):    
    @classmethod
    def sort(self, a):
        N = len(a)
        
        for i in xrange(N):
            index_min = i
            for j in xrange(i+1, N):
                if less(a[j], a[index_min]):
                    index_min = j
            exch(a, i, index_min)
            #show(a)
            
            
class Insertion(object):
    @classmethod
    def sort(self, a):
        N = len(a)
        
        for i in xrange(0, N-1):
            for j in xrange(i+1, 0, -1):
                if less(a[j], a[j-1]):
                    exch(a, j, j-1)
                else:
                    break
            #show(a)
            
            
class Shell(object):
    @classmethod
    def sort(self, a):
        N = len(a)
        
        h = 1
        while (h < N/3):
            h = h * 3 + 1
        while (h >= 1):                             # last one should be h=1
            for i in xrange(h, N):                  # sort from h
                for j in xrange(i, h-1, -h):        # j>=h in other language, but since the second parameter is not included, we use h-1 here
                    if less(a[j], a[j-h]):
                        exch(a, j, j-h)
                    else:
                        break                       # once a[j-h] <= a[j], stop this loop         
            h = h/3
            #show(a)
            
class Merge(object):
    @classmethod
    def merge(self, a, lo, mid, hi):
        i = lo; j = mid + 1                         # no need to use for loop to control i and j!!!!!!!!!!!!!!!!!!!!!!!!
        
        aux = a[:]
        
        for k in xrange(lo, hi + 1):                # xrange(hi+1) is totally wrong, and hi + 1 is the end of range, not just hi
            if i > mid:
                a[k] = aux[j]; j += 1
            elif j > hi:
                a[k] = aux[i]; i += 1
            elif less(aux[j], aux[i]):
                a[k] = aux[j]; j += 1
            else:
                a[k] = aux[i]; i += 1
            
    @classmethod
    def sort_topdown_helper(self, a, lo, hi):       # code I wrote, many mistakes
                                                    # N = len(a)               # sort part of array, N is meaningless here
        if hi <= lo:                                # if N == 0 or N == 1:
            return
        else:
            mid = lo + (hi - lo)/2                  # mid = (lo + hi)/2        # very important that the way we calculate the mid
            self.sort_topdown_helper(a, lo, mid)
            self.sort_topdown_helper(a, mid+1, hi)
            self.merge(a, lo, mid, hi)
    
    @classmethod
    def sort_topdown(self, a):
        self.sort_topdown_helper(a, 0, len(a)-1)
        
    @classmethod
    def sort_bottomup(self, a):        
        N = len(a)
        sz = 1
        while sz < N:                                               # try to maintain the sz less than N/2 + 2, no need to do that. "for sz in xrange(1, N, sz):" is wrong here, sz is always the value is assign at the beginning.
            for lo in xrange(0, N - sz, sz * 2):                    # the reason why use N - sz here because the number of remain items in the last less than sz, these items should be sorted in last loop.
                self.merge(a, lo, lo+sz-1, min(lo+sz*2-1, N-1))     # the mid could be calculate in a tricky way that we don't need to use hi.
            sz += sz
            
class Quick:
    @classmethod
    def sort_helper(self, a, lo, hi):
        if hi <= lo:
            return
    
        j = self.partition(a, lo, hi)
        self.sort_helper(a, lo, j-1)
        self.sort_helper(a, j+1, hi)
    
    @classmethod
    def partition(self, a, lo, hi):
        v = a[lo]
        i = lo+1; j = hi                    # the sample code in the book is i = lo, j = hi + 1 for using ++i and --j in below loop, but python doesn't support ++ and -- syntaxes. 
        
        while True:
            while less(a[i], v):
                if i == hi:
                    break
                i+=1   
            while less(v, a[j]):
                if j == lo:
                    break
                j-=1
            if j<=i:
                break
            exch(a, i, j)
        exch(a, lo, j)
        return j                            # it's easy to forget return j

    @classmethod
    def sort(self, a):
        self.sort_helper(a, 0, len(a)-1)
        
    @classmethod
    def sort_3way_helper(self, a, lo, hi):
        if hi <= lo:
            return
        
        lt = lo; i = lo + 1; gt = hi
        v = a[lo]
        while i <= gt:
            cmp = compareTo(a[i], v)
            if cmp < 0:
                exch(a, lt, i)
                lt += 1; i += 1
            elif cmp > 0:
                exch(a, gt, i)              # i will remain the same because it is changed with gt, and the item gt haven't been compared yet
                gt -= 1
            else:
                i += 1
        
        self.sort_3way_helper(a, lo, lt-1)
        self.sort_3way_helper(a, gt+1, hi)
                
        
    @classmethod
    def sort_3way(self, a):
        self.sort_3way_helper(a, 0, len(a)-1)
    
            
if __name__ == "__main__":
    arr = list("SORTEXAMPLE")
    Selection.sort(arr)
    print arr
    
    arr = list("SORTEXAMPLE")
    Insertion.sort(arr)
    print arr    
    
    arr = list("SORTEXAMPLE")
    Shell.sort(arr)
    print arr        
    
    
    arr = list("AEIOUBCDHK")
    Merge.merge(arr, 0, 4, 9)
    print arr
    
    arr = list("SORTEXAMPLE")
    Merge.sort_topdown(arr)
    print arr      
    
    arr = list("SORTEXAMPLE")
    Merge.sort_bottomup(arr)
    print arr     
    
    arr = list("SORTEXAMPLE")
    Quick.sort(arr)
    print arr       
    
    arr = list("SORTEXAMPLE")
    Quick.sort_3way(arr)
    print arr           
    
            