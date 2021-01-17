## Notes --> I tried to solve it but unable to understand it. Need to do it again.

# In this we are going to solve leetcode #779 problem
# https://leetcode.com/problems/k-th-symbol-in-grammar/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- N and K
  # Output -- Kth value in Nth row
  # Egde Cases -- first row and first element
  # Assumptions -- 

''' Pseudo code  --

'''

# Actual code --
# Solution 1: my naive solution (time limit exceeded in leetcode)

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        n = 1
        first = [0]
        second = []
        while N > n:
            for i in first:
                if i == 0:
                    second = second + [0,1]
                elif i == 1:
                    second = second + [1,0]
            first = second
            second = []
            n = n+1
        print(first)
        return first[K-1]

'''

Leetcode statistics -- 
Runtime: 72 ms
Memory Usage: 14.3 MB
'''
