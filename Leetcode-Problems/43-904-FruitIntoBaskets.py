# In this we are going to solve leetcode #904 problem
# https://leetcode.com/problems/fruit-into-baskets/

''' Pattern : this question can be solved using following pattern
## all these technique solutions available on leetcode

# sliding window pattern
# two pointer technique
# four pointer technique
'''

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input --
  # Output --
  # Egde Cases --
  # Assumptions --

''' Pseudo code  --

'''

# Actual code --
# Solution 1:

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        notes: k is always 2
        tree array can't be empty

        '''
        windowStart = 0
        windowElement = {}
        maxFruits = float('-inf')

        for i, v in enumerate(tree):

            if v not in windowElement:
                windowElement[v] = 1
            else:
                windowElement[v] += 1

            while len(windowElement.keys()) > 2:
                windowElement[tree[windowStart]] -= 1
                if windowElement[tree[windowStart]] == 0:
                    del windowElement[tree[windowStart]]
                windowStart += 1

            maxFruits = max(maxFruits, sum(windowElement.values()))

        return maxFruits

''' Big-O efficiency
time complexity - O(n) - because of for loop for entire array
space complexity - O(1) - it will alaways be having 2 unique elements
memory - 20 MB
Runtime - 1092 ms (12.40 % faster only)
'''

# Solution 2:
