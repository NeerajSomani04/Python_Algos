# In this we are going to solve leetcode #70 problem
# https://leetcode.com/problems/climbing-stairs/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an integer represent the steps in a stair that you need to climb
  # Output -- return integer that represents in how many distinct ways can you climb to the top?
  # Egde Cases -- 
  # Assumptions -- 1 <= n <= 45

''' Pseudo code  --
      
'''

# Actual code --
# Solution 1:

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = {1:1, 2:2, 3:3}
        
        def temp_cal(n):
            if n in temp:
                return temp[n]
            cal = temp_cal(n-1) + temp_cal(n-2)
            temp[n] = cal
            return cal
        
        return temp_cal(n)
 '''
 Big-O efficiency
 time complexity - O(n) --> because of n recursive calls
 space complexity - O(n) --> because of dictionary
 '''
