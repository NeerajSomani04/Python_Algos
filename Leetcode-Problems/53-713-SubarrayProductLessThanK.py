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
 
 # Solution 2 -- this is solution from leetcode
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
            print(ans)
        return ans

'''
Big-O complexity 
Time Complexity: O(N), where N is the length of nums. left can only be incremented at most N times.

Space Complexity: O(1), the space used by prod, left, and ans.
'''


# Solution 3 - for a followup problem, if we need to return all array elements as well.
# this solution is from grokking the coding

#answer
from collections import deque


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from lef to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

'''
Time complexity 
The main for-loop managing the sliding window takes O(N)but creating subarrays can take up to O(N^2) in the worst case. 
Therefore overall, our algorithm will take O(N^3).
Space complexity 
Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.
At the most, we need a space of O(n^2) for all the output lists.
'''

