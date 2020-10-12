# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question

Data - 
  - Input - a fixed length array that contains some intergers
  - output - function should modify the array in-place, should not return anything
  - Edge case - no zero at all in the array, at-least 1 element will be in array, zero could be last element in the array, or a zero present on the boundary of the leftover elements.
  - assumptions - 
  
Pseudo code - 
  - read array and count number of zero's that needs to be duplicated.
    - here, edge case, would be, don't duplicate zero's that are coming at the boundry of the array
  - read the array in reverse order and copy zero twice and non-zero once
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
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            ## this below line is moving each non-zero element to the non-empty space towards end of an array
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            ## if we hit any zero, we need to duplicate its value (or copy it twice)
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

                    
## Big-O efficiency -
# time complexity - O(n) --> because of count function O(n) ,  then because of for loop O(n)
# space complexity - O(1) --> no extra memory used


# space complexity - O(1) --> no additional memory used.

