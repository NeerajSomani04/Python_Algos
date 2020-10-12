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
# Solution 1:
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False     
        else:
            max = 0
            max_index = 0
            result = False
            for i, value in enumerate(A):
                if value > max:
                    max = value
                    max_index = i
            if A.count(max) != 1 or max_index == len(A)-1 or max_index == 0:
                return False
            else:
                prev_val = max
                for j in range(max_index-1, -1, -1):
                    if A[j] >  prev_val:
                        return False
                    else:
                        result = True
                    prev_val = A[j]
                    #print('prev_val=', prev_val, 'result=', result)
                prev_val = max
                for k in range(max_index+1, len(A)):
                    if prev_val > A[k]:
                        result = True
                    else:
                        return False
                    prev_val = A[k]
                    #print('prev_val=', prev_val, 'result=', result)
        return result

''' Big-O efficiency -
# time complexity - O(n) -- because of count function and for loop
# space complexity - O(1) 
'''
