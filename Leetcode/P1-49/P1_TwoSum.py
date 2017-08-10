class Solution(object):
    def twoSum_my(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lt = [x for x in nums if x <= target/2]
        gt = [x for x in nums if x >= target/2]
        
        for i in lt:
            for j in gt:
                if i+j == target:
                    if i==j:
                        if nums.count(i) <= 1:
                            continue
                        else:
                            index1 = nums.index(i)
                            index2 = nums.index(j, index1 + 1)
                            return [index1, index2]
                    return [nums.index(i), nums.index(j)]
                
    def twoSum_a(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        d = {}
        i = 0
        
        # put the list into dictionary
        for x in nums:
            d[x] = i    # not d[i] = x for looking for existence in d by x 
            i+=1
        
        for i in xrange(len(nums)):  # cannot use "for x in nums:" since there will be miss if we have a list [3, 2, 3] and target 6
            complement = target - nums[i]
            if d.has_key(complement) and d[complement] != i:
                return [i, d[complement]]
            
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        d = {}
        
        for i in xrange(len(nums)):
            complement = target - nums[i]
            if d.has_key(complement):
                return [d[complement], i]
            d[nums[i]] = i
                
                
if __name__ == "__main__":
    a = [3, 2, 3]
    b = 6
    print Solution().twoSum(a, b)