## 162 - https://leetcode.com/problems/find-peak-element/

# Solution 1:
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end)//2
            
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid+1
        return start

'''
Time complexity #
Since we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.

Space complexity #
The algorithm runs in constant space O(1).
'''
