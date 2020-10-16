# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/)
Data - 
  - Input - two input string "needle" and "haystack"
  - output - Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
  - Edge case - What should we return when needle is an empty string? This is a great question to ask during an interview. 
        -- we will return 0 when needle is an empty string
  - assumptions - 
  
  
Pseudo code - 
  - 
'''

# Actual Code 
# Solution 1 -
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(haystack) == 0:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            #print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

''' Big-O efficiency 
# time complexity - O(n * h) - because of for loop and
   - When you slice the string like haystack here for example, you're creating a copy of the string. Sure it's only the size of needle, but just wanted to point out. The string comparison is O(n) where n is size of needle so solution is O(n * h) at best where h is size of haystack.
# space complexity - O(1)
'''


## Need to understand "KMP" algorithm to solve this problem by O(n) time complexity. YouTube it easily.
