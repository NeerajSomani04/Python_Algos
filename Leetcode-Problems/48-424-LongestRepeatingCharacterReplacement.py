# 424 - https://leetcode.com/problems/longest-repeating-character-replacement/

'''
Input - string, contains only uppercase english letters, and
  - k, an interger, that represents allowed replacement operations
Output - an interger, that represents longest possible sub-string with all repeating letters, after k operations
Edge cases - an empty string, 
  - k operations not possible to perform
assumptions - contains only english charachters
Constraints -
'''

# Solution 1:
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart = 0
        max_len = 0
        ht = {}
        cnt = 0
        
        for windowEnd in range(len(s)):
            if s[windowEnd] in ht:
                ht[s[windowEnd]] += 1
            else:
                ht[s[windowEnd]] = 1
            
            cnt=max(ht.values())
            
            while windowEnd - windowStart + 1 - cnt > k:
                ht[s[windowStart]] -= 1
                windowStart += 1
            
            max_len=max(max_len, sum(ht.values()))
        return max_len

''' Big-O notation
time complexity - O(n)
space complexity - O(1) - at max we can have only 26 english char in a hash table
Leetcode statistics -
memory - 14 MB
runtime - 172 ms (better than only 35%)
'''

# Solution 2:
