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
# Solution 1:
