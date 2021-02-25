# 386 - https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/

'''
Input - a string and an integer that represent number of possible distinct char in a sub-string
output - the length of the longest substring that satisfies k
edge - no such substring, for example k is too large, return 0
  - if k is 0, then return 0
  - if string empty, return 0
assumption - 
'''

# soultion 1
import math
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if k == 0 or len(s) == 0:
            return 0
        ht = {}
        windowStart = 0
        result = -math.inf
        for windowEnd in range(len(s)):
            if s[windowEnd] in ht:
                ht[s[windowEnd]] += 1
            else:
                ht[s[windowEnd]] = 1
            while len(ht) >= k:
                print(ht)
                result = max(result, sum(ht.values()))
                if ht[s[windowStart]] == 1:
                    del ht[s[windowStart]]
                else:
                    ht[s[windowStart]] -= 1
                windowStart += 1
        if result == -math.inf:
            return 0
        else:
            return result
        
        # time complexity - O(n)
        # space complexity - O(k)
