"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        length1 = len(nums1)
        length2 = len(nums2)
        
        
        N = length1 + length2
 
            
        i = 0; j = 0
        for x in xrange((N-1)/2):
            if i >= length1 :
                j+=1
            elif j >= length2  or nums1[i] <= nums2[j]:                # j >= length2  must comes first
                i+=1
            else:
                j+=1
                
        if N % 2 == 1:
            return min(nums2[j] if i >= length1 else nums1[i], nums1[i] if j >= length2 else nums2[j])
        else:
            if i >= length1:
                return (nums2[j] + nums2[j+1]) / 2.0
            elif j >= length2:
                return (nums1[i] + nums1[i+1]) / 2.0
            else:
                n1 = 0; n2 = 0
                if nums1[i] <= nums2[j]:
                    n1 = nums1[i]
                    i += 1
                else:
                    n1 = nums2[j]
                    j += 1
                    
                if i >= length1:
                    n2 = nums2[j]
                elif j >= length2:
                    n2 = nums1[i]
                else:
                    n2 = min(nums1[i], nums2[j])    

                    
                return (n1 + n2) / 2.0
                
        
if __name__ == "__main__":
    a1 = [1]
    a2 = [2, 3, 4, 5]
    print Solution().findMedianSortedArrays(a1, a2)
    
    a1 = []
    a2 = [2, 3, 4, 5]    
    print Solution().findMedianSortedArrays(a1, a2)
    
    a1 = []
    a2 = [1]    
    print Solution().findMedianSortedArrays(a1, a2)  
    
    a1 = [1]
    a2 = [1]    
    print Solution().findMedianSortedArrays(a1, a2)        
        
        
        
        