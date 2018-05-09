import numpy as np
import statistics as st

if __name__ == "__main__":
    a = np.array([1,2,3,4,5,6,7])
    b = np.array([2.25,2.25,2.25,2.25,2.25,2.25,2.25,2.25])
    
    print np.mean(a)
    print np.std(a)         # population standard deviation, ddof = 0
    
    print st.mean(a)
    print st.stdev(a)       # ddof = 1, that means it equals that np.std(a, ddof=1)