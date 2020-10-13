# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question - (https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/)
Data - 
  - Input - an array that contains some intergers
  - output - return modified array
  - Edge case - array length 1
  - assumptions - 
  
Pseudo code - 
  - if array length 1, then replace with -1 and return
  - else, go through each element of array 
'''

# Actual Code 
# Solution 1 -
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_pointer = 0
        for i, value in enumerate(A):
            if value % 2 == 0:
                A[even_pointer], A[i] = A[i], A[even_pointer]
                even_pointer += 1
        return A

''' Big-O efficiency -
# time complexity - O(n) - because of for loop
# space complexity - O(1) 
'''
