# 137 - 

# Solution 1: this is best solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # approach 2:
        n = len(nums)
        if n < 2:
            return nums[0]
        nums.sort()
        print(nums)
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[n-1] != nums[n-2]:
            return nums[n-1]
        else:
            i = 1
            while i < n:
                if nums[i] == nums[i-1]:
                    i = i+3
                else:
                    return nums[i-1]
        
'''
time complexity - O(n log n) --> here, (log n) <= 32 
    -- mentioned this because bit manipulation is going to take O(32 * n) time complexity.
space complexity - O(n)
'''



# Solution 2:
ht = {}
for i in nums:
    if i in ht:
        ht[i] += 1
    else:
        ht[i] = 1

for i in ht:
    if ht[i] == 1:
        return i

'''
time complexity - O(n)
space complexity - O(n)
'''
        
    
