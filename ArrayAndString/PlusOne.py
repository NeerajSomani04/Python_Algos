# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/)
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
# solution 1 -
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join(map(str, digits))
        digits = str(int(digits)+1)
        digits = list(map(int,digits))
        print(digits)
        return digits

''' Big-O efficiency
# time complexity - O(n)
# space complexity - O(1)
'''
