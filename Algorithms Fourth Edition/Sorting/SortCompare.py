import time
import SortingAlgorithms as sa
import random

class SortCompare(object):
    @classmethod
    def time(self, alg, a):
        start = time.time()
        if (alg == "Selection"): 
            sa.Selection.sort(a)
        elif (alg == "Insertion"): 
            sa.Insertion.sort(a)
        elif (alg == "Shell"): 
            sa.Shell.sort(a)
        elif (alg == "Merge_topdown"): 
            sa.Merge.sort_topdown(a) 
        elif (alg == "Merge_bottomup"): 
            sa.Merge.sort_bottomup(a) 
        elif (alg == "Quick"): 
            sa.Quick.sort(a) 
        elif (alg == "Quick_3way"): 
            sa.Quick.sort_3way(a)          
        end = time.time()
        
        return end - start
    
    
    @classmethod
    def timeRandomInput(self, alg, N, T):
        total = 0.0
        for t in xrange(T):
            a = [None] * N
            for i in xrange(N):
                a[i] = random.uniform(0, 1)
            total += self.time(alg, a)
        return a, total
    

if __name__ == "__main__":
    a, t = SortCompare.timeRandomInput("Selection", 1000, 1)
    print "Selection      \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)
    a, t = SortCompare.timeRandomInput("Insertion", 1000, 1)
    print "Insertion      \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)
    a, t = SortCompare.timeRandomInput("Shell", 1000, 1)
    print "Shell          \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)
    a, t = SortCompare.timeRandomInput("Merge_topdown", 1000, 1)
    print "Merge_topdown  \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)
    a, t = SortCompare.timeRandomInput("Merge_bottomup", 1000, 1)
    print "Merge_bottomup \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)  
    a, t = SortCompare.timeRandomInput("Quick", 1000, 1)
    print "Quick          \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)  
    a, t = SortCompare.timeRandomInput("Quick_3way", 1000, 1)
    print "Quick_3way     \tSorted: " + str(sa.isSorted(a)) + "\tTime: " + str(t)     

    
            
