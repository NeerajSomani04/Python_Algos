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
