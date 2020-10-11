## As per Aaron - this is the most important Algorithm to understand for coding interviews
  # why because, a sorted array can be solved using binary search algorithm, which is efficient of O(log n)

# In this we are going to solve leetcode #35 problem
# https://leetcode.com/problems/search-insert-position/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a sorted array of distinct integers and a target value
  # Output -- return the index if the target is found. If not, return the index where it would be if it were inserted in order.
  # Egde Cases -- target value could be smaller or larger than all values of array, which makes index 0 or n+1
  # Assumptions -- no empty array and no duplicates in array

## Binary Search Algorithm is a great way to solve this problem
 ## why, because, It allows to search through a sorted array in O(log n) time complexity. 

'''
Naive Solution - Scan through the array and find out the place where the target value needs to be, but
time complexity in that case would be O(n). Can we do better.
Yes, using binary search Algo, we can make time complexity to solve this problem would be O(log n)
'''

''' Pseudo code  --
    initialize low and high pointers
    while low <= high
      - calculate mid pointer
      - compare mid value to target, if mid index value equals target return index
      - if target greater than mid value, low = mid + 1
      - if target less than mid value, hi = mid - 1
'''

  
    
    
# Actual code --
## Solution 1: (naive solution)
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

# best possible solution --
## Solution 2 -


''' Big-O Efficiency:
# time complexity - O(log n) because of BSA
# space complexity - O(1) -- no extra memory needed other than for few variables
'''
