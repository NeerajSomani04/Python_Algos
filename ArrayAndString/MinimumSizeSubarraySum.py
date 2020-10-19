# Solution 1 -
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        final_count = float('inf')
        for i, value in enumerate(nums):
            if value >= s:
                return 1
            for j in range(i+1, len(nums)):
                c = 1
                sum = value
                while sum < s:
                    sum += nums[j]
                    c += 1
            final_count = min(c, final_count)
        return final_count

'''Big-O efficiency -
time complexity - O(n * n) - because of two for loops
space complexity - O(1)
'''

# Solution 2 -
