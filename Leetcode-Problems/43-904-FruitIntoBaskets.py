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

# the other way of writing the same solution:
# 904 - https://leetcode.com/problems/fruit-into-baskets/

'''
Input - an int array 
    # k is always 2 in this problem
    # here array represensts the distinct type of fruit
output - an integer, that gives maxium number of fruit
'''


import math
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # k is always 2 in this problem
        # here array represensts the distinct type of fruit
        # we need to understand best place to start picking up so that we can collect maximum fruit        
        ht = {}
        windowStart = 0
        result = -math.inf
        for windowEnd in range(len(tree)):
            if tree[windowEnd] in ht:
                ht[tree[windowEnd]] += 1
            else:
                ht[tree[windowEnd]] = 1
            while len(ht) > 2:
                if ht[tree[windowStart]] == 1:
                    del ht[tree[windowStart]]
                else:
                    ht[tree[windowStart]] -= 1
                windowStart += 1
            result = max(result, sum(ht.values()))
        if result == -math.inf:
            return 0
        else:
            return result

'''
Big-O efficiency 
time complexity - O(n) - because of for loop
space complexity - O(k) - considering hash table will always be needed to store type of fruit
'''

