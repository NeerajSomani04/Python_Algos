# In this we are going to solve leetcode #912 problem
# https://leetcode.com/problems/sort-an-array/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array of integers
  # Output -- return a sorted array of integers
  # Egde Cases -- empty array as input
  # Assumptions -- need to implement an efficient sorting algorithm
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 


''' Psudo code
  - if array size 1, return
  - else, split left and right
  - merge, sorted sub-arrays by:
    - set L and R pointers
    - while L and R pointers have room
      - add lower value and advance
    - dump item from unfinished array
  - return final array
'''

## Different approach
## Solution 1: using recursion and Depth First Search

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        
    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        block = []
        l = r = 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                block.append(left[l])
                l += 1
            elif right[r] < left[l]:
                block.append(right[r])
                r += 1
            
        if l < len(left):
            block += left[l:]
        elif r < len(right):
            block += right[r:]
        
        return block

## Big-O-efficiency -->
## time complexity --> O(n log n) --> as we are dividing array into half, merge sort function will work as log n and we are traversing append for each element, meaning n element. 

## Space complexity --> O(n) -->
          --> sub-array as aurgument
          --> merge-sort recursive function call stack frame --> n/2 + n/4 + n/8 + ..... + n/n --> approaching n

## Note:--> time limit exceeded for this solution on leetcode






