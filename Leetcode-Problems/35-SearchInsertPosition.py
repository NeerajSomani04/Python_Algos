## As per Aaron - this is the most important Algorithm to understand for coding interviews
  - why because, a sorted array can be solved using binary search algorithm, which is efficient of O(log n)

# In this we are going to solve leetcode #35 problem
# https://leetcode.com/problems/search-insert-position/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a sorted array of distinct integers and a target value
  # Output -- return the index if the target is found. If not, return the index where it would be if it were inserted in order.
  # Egde Cases -- target is smaller or larger than any value in array
  # Assumptions -- no duplicates in array

## Pointer menthod or Pointer Traversal is a great way to solve this problem


''' Pseudo code  --
       
'''

  
    
    
# Actual code --
## Solution 1: 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            for i, value in enumerate(nums):
                if value >= target:
                    return i

## Big-O efficiency
# time complexity - O(n) - because of for loop
# space complexity - O(1)
