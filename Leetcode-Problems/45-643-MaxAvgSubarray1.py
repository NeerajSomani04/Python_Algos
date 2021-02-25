# Leetcode 643 --> Maximum Average Subarray I --> https://leetcode.com/problems/maximum-average-subarray-i/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

'''
Input - an array of size n, and an integer to represent sub-array size k
Output - max of average of k-size subarray
Edge Case - nothing
Assumption - Array can't be empty
'''

# Solution 1 -
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        windowStart = 0
        windowSum = 0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k-1:
                temp_avg = windowSum/k
                if max_avg < temp_avg:
                    max_avg = temp_avg
                windowSum -= nums[windowStart]
                windowStart += 1
        return max_avg

# Leetcode statistics
# memory used - 18.5 MB
# time taken - 856 ms

# Solution 2 - slightly better way of writting code
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      best = now = sum(nums[:k])
      for i in range(k,len(nums)):
          now += nums[i] - nums[i-k]
          if now>best:
              best = now
      return best/k
    
# Leetcode statistics
# memory used - 18.1 MB
# time taken - 762 ms  
