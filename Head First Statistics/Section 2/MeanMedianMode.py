import numpy as np
import statistics as st     # statistics need to be installed in python 2.7, pip install statistics

if __name__ == "__main__":
    a = np.array([1,1,2,2,2,3,3,4])
    print np.mean(a)        # average could compute a weighted average
    print np.median(a)
    #print np.mode(a)       # no this function
    
    print st.mean(a)
    print st.median(a)
    print st.mode(a)