# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/)
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


# Solution 1 -
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = []
        for value in nums:
            if len(temp) < 3 and value not in temp:
                temp.append(value)
                #print('inside if', temp)
            elif value > min(temp) and value not in temp:
                temp.append(value)
                temp.remove(min(temp))
                #print('inside elif', temp)
        temp = sorted(temp)
        return max(temp) if len(temp) < 3 else temp[0]


''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1)
'''

# Solution 2 -
class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]

''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1)
'''
