# 442 -- https://leetcode.com/problems/find-all-duplicates-in-an-array/


# Solution 1: this is iterative approach
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        index = 0
        result = []
        
        while index < len(nums):
            expected_value = index + 1
            target_value = nums[index] - 1
            if nums[index] != expected_value and nums[target_value] != nums[index]:
                nums[index], nums[target_value] = nums[target_value], nums[index]
            else:
                index += 1
        
        for i, v in enumerate(nums):
            if i+1 != v:
                result.append(v)
        
        return result
        
'''
time complexity - O(n)
space complexity - O(1)
'''

# Solution 2: Need to solve same using binary approach

