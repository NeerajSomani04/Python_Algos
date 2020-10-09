# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question

Data - 
  - Input - a fixed length array that contains some intergers
  - output - function should modify the array in-place, should not return anything
  - Edge case - no zero at all in the array, at-least 1 element will be in array, zero could be last element in the array, or a zero present on the boundary of the leftover elements.
  - assumptions - 
  
Pseudo code - 
  - read array
'''

# Actual Code 
# Solution 1 -
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        print(arr)
        
        len_ = len(arr)
        i = 0
        while( i < len_):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
                continue
            else:
                i += 1
        print(arr)

# Big-O efficiency -
# time complexity - O(n^2) --> while loop is O(n) and insert operation is O(n)
# space complexity - O(1) --> no extra space needed.

# Solution 2 -
