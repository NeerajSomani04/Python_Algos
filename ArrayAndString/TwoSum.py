# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/)
Data - 
  - Input - a sorted array that contains some intergers, and a target value
  - output - return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
            -- Your returned answers (both index1 and index2) are not zero-based.
  - Edge case - is it possible there wouldn't be any solution in input array
  - assumptions - array can't be empty
                -- You may assume that each input would have exactly one solution and you may not use the same element twice.
                -- no duplicate values
                -- Constraints:
                    2 <= nums.length <= 3 * 104
                    -1000 <= nums[i] <= 1000
                    nums is sorted in increasing order.
                    -1000 <= target <= 1000
  
  
Pseudo code - 
  - 
'''

# Actual Code 
# solution 1 -
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ht = {}
        result = []
        for i, value in enumerate(numbers):
            needed = target - value
            if needed in ht:
                result.append(ht[needed]+1)
                result.append(i+1)
                result.sort()
                return result
            else:
                ht[value] = i

'''Big-O efficiency -
time complexity - O(n) - because of for loop
space complexity - O(n) - because of hash table
'''

# Solution - 2
