# In this we are going to solve leetcode #136 problem
# https://leetcode.com/problems/single-number/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array of integers
  # Output -- single interger (that unique single number)
  # Egde Cases -- 
  # Assumptions -- Each element in the array appears twice except for one element which appears only once.

''' Pseudo code  --
      few naive solution thoughts -
      1. create hash table and store count, return the one that has only one. space and time complexity is O(n)
      2. sort the array and return as soon as you find the uniue number, space complexity - O(1) but time complexity O(n log n)
      3. 
'''

# Actual code --
# Solution 1: hash table solution
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

''' Big-O efficiency
Space complexity - O(n) - because of hash table
time complexity - O(n) - because of for loop
'''

# Solution 2: sort array and then loop through
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        result = list()
        while i < len(nums):
            if nums[i-1]==nums[i]:
                nums.pop(i)
                nums.pop(i-1)
                i-=1
            i+=1
        return nums[0]

''' Big-O efficiency
Space complexity - O(1) - because of hash table
time complexity - O(n long n) - because of for loop
runtime - 196 ms
memory utilization - 15.7 MB
'''

# Solution 3: math logic implementation 
class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

''' Big-O efficiency
Space complexity - O(n) - because of hash table
time complexity - O(n) - because of for loop
runtime - 132 ms
memory utilization - 16.7 MB
'''

# Solution 4: Bit manipulation
class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a

''' Big-O efficiency
Space complexity - O(1) - because of hash table
time complexity - O(n) - because of for loop
runtime - 128 ms
memory utilization - 16.5 MB
'''
