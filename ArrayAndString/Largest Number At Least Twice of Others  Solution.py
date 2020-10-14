# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/)
Data - 
  - Input - a array that contains some intergers
  - output - return index of largest element as per question description
  - Edge case - 
  - assumptions - array can't be empty, there wouldn't be any duplicates
  
  
Pseudo code - 
  - 
'''

# Actual Code 
# Solution 1 -
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = 0
        for i, value in enumerate(nums):
            if value == largest:
                index = i 
            elif value*2 > largest and value != largest:
                return -1
        return index

''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1) 
'''
