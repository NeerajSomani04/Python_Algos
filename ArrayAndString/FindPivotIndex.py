# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/)

Data - 
  - Input - a array that contains some intergers
    Constraints:
      - The length of nums will be in the range [0, 10000].
      - Each element nums[i] will be an integer in the range [-1000, 1000]
  - output - return left most pivot index
  - Edge case - array can be empty, no pivot index in array
  - assumptions - 
  
Pseudo code - 
  - if length of array is less than 3:
      - return -1
  - 
'''

# Actual Code 
# Solution 1 -
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
        
'''

''' Big-O efficiency 
# time complexity - O(n) - because of sum function and for loop
# space complexity - O(1)
'''
