# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/two-sum/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
  # Output -- Find all unique triplets in the array which gives the sum of zero.
  # Egde Cases -- array can be empty, the solution set must not contain duplicate triplets. There is no thiplets that satisfies this.
  # Assumptions -- input can have duplicate numbers, output triplet must be unique, triplet order doesn't matter.
    Constraints:
        0 <= nums.length <= 3000
        -105 <= nums[i] <= 105


''' Pseudo code  --
      - sort the array
      - for every number in nums
        - while left < right
            - if sum is too low, increase left by 1 
            - if sum is too high, decrease right by 1
            - if we find zero, add to output, and move both pointer
'''

# Actual code --
## Solution 1: this is copy of Aaron's approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            left = i+1
            right = length-1
            if i>0 and nums[i-1] == nums[i]: continue 
            ## remember, our array is sorted and hence all duplicate values will be together, above if statement will help us to get rid of all those duplicate value.
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i] , nums[left] , nums[right]])
                    # if we use set to avoid duplicate entries, that would be easy, but since we are using array,
                    # need to add below lines, to avoid duplicates
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total>0:
                    right -= 1
                else:
                    left += 1
        return output  

'''Big-O efficiency 
# time complexity - O(n*n) --> O(n log n) because of sort + O(n) * O(n) because of for and while loop
# space complexity - O(1) - if we consider only variables
    - else, O(n) - if we consider output array as well
'''

## Solution - 2 - (Using set to avoid duplicate entries)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        length = len(nums)
        for i in range(length):
            left = i+1
            right = length-1
            if i>0 and nums[i-1] == nums[i]: continue 
            ## remember, our array is sorted and hence all duplicate values will be together, above if statement will help us to get rid of all those duplicate value.
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.add((nums[i] , nums[left] , nums[right]))
                    # if we use set to avoid duplicate entries, that would be easy, but since we are using array,
                    # need to add below lines, to avoid duplicates
                    '''
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    '''
                    left += 1
                    right -= 1
                elif total>0:
                    right -= 1
                else:
                    left += 1
        return output    

'''Big-O efficiency 
# time complexity - O(n*n) --> O(n log n) because of sort + O(n) * O(n) because of for and while loop
# space complexity - O(1) - if we consider only variables
    - else, O(n) - if we consider output array as well
'''

