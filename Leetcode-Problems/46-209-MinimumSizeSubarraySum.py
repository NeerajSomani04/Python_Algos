# Leetcode 209 --> Maximum Average Subarray sum --> https://leetcode.com/problems/minimum-size-subarray-sum/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

'''
Input - an array of size n, and an integer to represent sub-array sum k
Output - an interger that represent count of subarray elements
Edge Case - if no such sub-array, then return 0
Assumption - Array can't be empty
'''

# Solution 1 -
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        final_count = math.inf 
        windowStart = 0
        windowSum = 0
        temp_count = 0
        for windowEnd in range(len(nums)): 
            windowSum += nums[windowEnd]
            temp_count += 1
            while windowSum >= target:
                final_count = min(temp_count, final_count)
                windowSum -= nums[windowStart]
                windowStart += 1
                temp_count -= 1    
        if final_count == math.inf:
            return 0
        else:
            return final_count

'''
Big-O efficiency:
time complexity - O(n) - because we are iterating all elements in an array
space complexity - O(1) - because we using only few variables and not any data structures
Leetcode statistics:
memory: 16.4 MB
time: 76 ms
faster than 59.69%
'''

# Solution 2 - need to try to implement it using binary search.

