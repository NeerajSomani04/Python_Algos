# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Solution 1: iteratively
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

# Solution 2: recursively

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:                        
        result = [i for i in range(0, len(nums)+1)] # build an array (0, 1, 2, 3, ..., n)
        for i in nums: result[i] = 0 # we index this array, setting "found" elements to zero
        return [i for i in result if i != 0] # we return results that aren't zero

# Solution 3: recursively but in fewer lines of code
def findDisappearedNumbers(self, nums):
        missing = set(range(1,len(nums)+1))
        nums = set(nums)
        missing = list(missing.difference(nums))
        return missing
