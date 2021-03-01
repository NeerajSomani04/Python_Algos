# 713 - https://leetcode.com/problems/subarray-product-less-than-k/

'''
        Input -- an array of positive integers
        Output -- an interger, that represents 
        edge cases -- array can be empty, return 0, 
            -- repeatitive numbers could be there or not, need to handle it
        assumptions -- if sum == k, is not considered
        Constraints --
            -- 0 < nums.length <= 50000.
            -- 0 < nums[i] < 1000.
            -- 0 <= k < 10^6
        '''
        
        '''
        thought process -->
            -- window enlarge as much as possible
            -- its a question of combination mathematical concept
            -- 
        '''

# Solution 1: This is not the correct solution, because time limit exceed

import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        windowStart = 0
        result = 0
        for windowEnd in range(n):   
            while windowEnd < n:
                total = math.prod(nums[windowStart:windowEnd+1])
                ## above line is not good, because we are reevaluation product many times.
                ## hence time limit exceeded
                if total < k:
                    result += 1
                    windowEnd += 1
                else:
                    windowStart += 1
                    break

        return result
        
 '''
 Big-O 
 time complexity --> O(n^2) - because of for loop
 space complexity --> O(1) 
 '''
 
 # Solution 2 --
