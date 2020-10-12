# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/)

Data - 
  - Input - a sorted array that contains some intergers
  - output - return new array length after removing duplicates
  - Edge case - empty array or no duplicates at all
  - assumptions - 
  
Pseudo code - 
  - start your process only if array is not empty
  - take first element of array into a variable for comparision with next element
  - create another counter for new array length
  - move only non-duplicate elements of array towards start of the array
'''

# Actual Code 
# Solution 1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) >= 1:     
            prev_val = nums[0]
            j = 1
            new_array_len = 1
            for i in range(1,len(nums)):
                if prev_val != nums[i]:
                    nums[j] = nums[i]
                    j += 1
                    prev_val = nums[i]
                    new_array_len += 1
            return new_array_len

''' Big-O efficiency:
# time complexity - O(n) - because of for loop
# space complexity - O(1) - 
'''
