## 34 - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


# Solution 1:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        result[0] = self.BinarySearch(nums, target, False)
        if result[0] != -1:
            result[1] = self.BinarySearch(nums, target, True)
        return result
        
    def BinarySearch(self, nums: List[int], target: int, findKeyIndex: bool):
        keyIndex = -1
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else: # target == nums[mid]
                keyIndex = mid
                if findKeyIndex:
                    low = mid+1
                else:
                    high = mid-1
        
        return keyIndex
        

'''
Time complexity 
Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm 
will be O(logN) where ‘N’ is the total elements in the given array.
Space complexity 
The algorithm runs in constant space O(1).
'''

'''
