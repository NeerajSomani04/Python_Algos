# Solution 1:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        new_index = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                val_count += 1
            else:
                nums[new_index] = nums[i]
                new_index -= 1
        nums[:len(nums)-val_count:] = nums[val_count::]
        return len(nums)-val_count

''' Big-O efficiency:
time complexity - O(n) - because of for loop
space complexity - O(1) - constant space
'''
