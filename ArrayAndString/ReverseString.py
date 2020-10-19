# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/)
Data - 
  - Input - Given two binary strings, The input strings are both non-empty and contains only characters 1 or 0.
  - output - return string that contains sum of two input strings
  - Edge case - 
  - assumptions - Constraints:
        Each string consists only of '0' or '1' characters.
        1 <= a.length, b.length <= 10^4
        Each string is either "0" or doesn't contain any leading zero.
  
Pseudo code - 
  - 
'''

# Notes:- This question is completely out of my understanding right now. Will come to this later.

# Actual Code 
# Solution 1 -
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

'''Big-O efficiency 
time complexity - O(n) - because of while loop
space complexity - O(1) 
'''
