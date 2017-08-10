"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """ ************** 1: slow solution, but it can return the whole string ************** """
        #if s == "":
            #return 0
        
        #N = len(s)
        #a = [1] * N
        
        ##for j in xrange(1, N):
        #for i in xrange(1, N):
            #if s[i] in s[:i]:
                #a[i] = min(i - s[:i].rfind(s[i]), a[i-1]+1)
            #else:
                #a[i] = a[i-1] + 1
                
        #return max(a)
        
        
        
        #longestLength = max(a)
        #longestIndex = a.index(longestLength)
        #return s[longestIndex-longestLength+1:longestIndex+1]
        """ ************** 1: slow solution, but it can return the whole string ************** """
        
        
        """ ************** 2: faster solution ************** """
        #start = maxlength = 0
        #d = {}
        #for i in xrange(len(s)):
            #if s[i] in d and start <= d[s[i]]: start = d[s[i]] + 1
            #else: maxlength = max(maxlength, i - start + 1)
            #d[s[i]] = i
            
        #return maxlength
        """ ************** 2: faster solution ************** """
        
        
        """ ************** 3: try to use enumerate ************** """
        start = maxlength = 0
        d = {}
        for num, ch in enumerate(s):
            if ch in d and start <= d[ch]: start = d[ch] + 1
            else: maxlength = max(maxlength, num - start + 1)
            d[ch] = num
    
        return maxlength        
    
"""
abcabcbb
12312321

abcabcdbb
123123433

abcabcbdb
123123232

"""

if __name__=="__main__":
    print Solution().lengthOfLongestSubstring("abcabcbb")
    print Solution().lengthOfLongestSubstring("bbbbb")
    print Solution().lengthOfLongestSubstring("pwwkew")
    print Solution().lengthOfLongestSubstring("tmmzuxt")
                    