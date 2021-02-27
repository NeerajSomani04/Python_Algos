# 26 - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Remove Duplicates from Sorted Array

'''
Input - given a sorted array
output - return an interger, that represent new length of array after removing duplicates
edge case - empty array
assumptions - 
Constraints:
    needs to be done in-place
    no extra space should be used, like hash-table, set, etc
'''

# Solution 1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        array_len = len(nums)
        if array_len < 2:
            return array_len
        left, right = array_len-2, array_len-1
        new_arr_len = array_len
        for i in range(array_len-1):
            if nums[left] == nums[right]:
                nums.pop(right)
                new_arr_len -= 1
            left -= 1
            right -=1
        return new_arr_len


# Solution 2:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index of the next non-duplicate element
        next_non_duplicate = 1

        i = 1
        while(i < len(nums)):
            if nums[next_non_duplicate - 1] != nums[i]:
                nums[next_non_duplicate] = nums[i]
                next_non_duplicate += 1
            i += 1

        return next_non_duplicate

'''
Time Complexity 
The time complexity of the above algorithm will be O(N), 
where ‘N’ is the total number of elements in the given array.
Space Complexity 
The algorithm runs in constant space O(1).
'''
