

# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/two-sum/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- Given an array of integers nums and an integer target
  # Output -- return indices of the two numbers such that they add up to target
  # Egde Cases -- 
  # Assumptions -- assume that each input would have exactly one solution, and you may not use the same element twice.
    - You can return the answer in any order.
    Constraints:
      2 <= nums.length <= 105
      -109 <= nums[i] <= 109
      -109 <= target <= 109
      Only one valid answer exists.


''' Pseudo code  --
      compare original string with reverse of it 
'''

# Actual code --
## Naive Solution --
## Solution 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

''' Big-O efficiency -
# time complexity - O(n*n) - because of two for loops
# space complexity - O(1)
'''

# Solution 2 - Best possible solution -
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            counter_part = target - nums[i]
            if counter_part in table:
                return [table[counter_part],i]
            else:
                table[nums[i]] = i

''' Big-O efficiency 
# time complexity - O(n) - because of for loop
# space complexity - O(1) 
'''
