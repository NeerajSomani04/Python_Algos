# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/)
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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''
        first_ele = strs[0]
        flag = True
        result = ''
        for i in range(len(first_ele)):
            for j in strs:
                if j == '':
                    return ''
                elif i >= len(j):
                    return result
                elif j[i] != first_ele[i]:
                    flag = False
                    return result
            if flag == True:
                result += j[i]
        return result 

''' Big-O efficiency 
# time complexity - O(n * m) -- where n is number of values in strs and m is mininum elements that will match in each string.
# space complexity - O(m) - considering result will store those minimum elements to store.
'''

# Solution 2 -
# this can be solved by using recursion or BST.
# but looks like time complexity is same or worst than above solution. Need to solve this again with other approaches.

