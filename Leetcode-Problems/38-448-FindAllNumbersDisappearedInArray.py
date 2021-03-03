# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Solution 1: iteratively (discussed in interview espresso)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        p = 0 
        while p < len(nums):
            if nums[p] != -1:
                q = nums[p] - 1 # q appears
                while nums[q] != -1: 
                    new_q = nums[q] - 1 # before marking, store the information that nums[q] has
                    nums[q] = -1 # mark that q appears
                    q = new_q
            
            p += 1
       
	   # find the numbers that never appear
        p = 0 
        while p < len(nums):
            if nums[p]!= -1:
                res.append(p + 1)
            p += 1
        return res

'''
time complexity - O(n)
space complexity - O(1)
'''

# Solution 4: as per understanding from Grokking coding interview pattern
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        missing = []
        while index < len(nums):
            expected_value = 1 + index
            target_value = nums[index] - 1
            if nums[index] != expected_value and nums[target_value] != nums[index]:
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]
            else:
                index += 1
            
        
        for i, v in enumerate(nums):
            if i+1 != v:
                missing.append(i+1)
        return missing

'''
time complexity - O(n)
space complexity - O(1)
'''


# Solution 2:  taken from leetcode discussion

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:                        
        result = [i for i in range(0, len(nums)+1)] # build an array (0, 1, 2, 3, ..., n)
        for i in nums: result[i] = 0 # we index this array, setting "found" elements to zero
        return [i for i in result if i != 0] # we return results that aren't zero

'''
time complexity - O(n)
space complexity - O(n) - because of result array
'''

# Solution 3: taken from leetcode discussion
def findDisappearedNumbers(self, nums):
        missing = set(range(1,len(nums)+1))
        nums = set(nums)
        missing = list(missing.difference(nums))
        return missing

'''
time complexity - O(n)
space complexity - O(n) - because of missing set
'''
