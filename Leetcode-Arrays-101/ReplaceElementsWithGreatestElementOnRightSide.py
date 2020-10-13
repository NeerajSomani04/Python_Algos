# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question - (https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/)

Data - 
  - Input - an array that contains some intergers
  - output - return modified array
  - Edge case - array length 1
  - assumptions - 1 <= arr.length <= 10^4 and 1 <= arr[i] <= 10^5
  
Pseudo code - 
  - if array length 1, then replace with -1 and return
  - else, go through each element of array 
'''

# Actual Code 
# Solution 1 -
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:        
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        return arr

''' Big-O efficiency
# time complexity - O(n*n) -- because of for loop and max function
# space complexity - O(1)
'''

# Solution 2 -
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        hi = -1
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                hi = arr[i]
                arr[i] = -1
            else:
                temp_hi = hi
                if arr[i] > hi:
                    hi = arr[i]
                arr[i] = temp_hi
        
        return arr

''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1) 
'''
