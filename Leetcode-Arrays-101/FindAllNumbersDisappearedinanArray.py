# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/)
Data - 
  - Input - a array that contains some intergers
  - output - return third maximum number in array
  - Edge case - number can vary from any negative to position number, array length can be one to infinity.
  - assumptions - array can't be empty
  
Pseudo code - 
  - create an empty array that contains only 3 maximum element at any iteration of nums array
  - run through each element of array and check if new element is greater than min(array) 
    - replace it
    - return third max of array after sorting it
'''

# Actual Code 

'''
# NOTES for myself -
Not able to solve it by myself. After understanding other Solutions from Discussion, I realized a very critical point of this question:-
  -- any element inside the array can't be greater than the size of array, meaning:
  -- this example is not valid array for this question :- [1, 2, 7], because 'n'=3, (n = size of array), and 7 can't be a part of this array for this question.
  -- Also, some elements appear twice and others appear once, meaning non element can appear more than two times.
  -- Now, I can think and better understand about the solution provided in discussion
'''

# Solution 1 -
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res

''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1) 
'''
