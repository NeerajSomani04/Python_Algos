# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question - (https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/)
Data - 
  - Input - an array that contains some intergers
  - output - return modified array
  - Edge case - array length 1
  - assumptions - 
  
Pseudo code - 
  - if array length 1, then replace with -1 and return
  - else, go through each element of array 
'''

# Actual Code 
# Solution 1 -

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums        
        zero_pointer = 0
        for i,value in enumerate(nums):
            if zero_pointer < len(nums):
                if value != 0:
                    nums[i], nums[zero_pointer] = 0, nums[i]
                    zero_pointer += 1
        return nums
