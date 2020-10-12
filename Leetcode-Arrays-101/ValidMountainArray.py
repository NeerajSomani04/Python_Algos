# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/)


Data - 
  - Input - an array that contains some intergers
  - output - return true if it satisfies all condition of mountain array, else return False
      -- Recall that A is a mountain array if and only if:
            - A.length >= 3
            - There exists some i with 0 < i < A.length - 1 such that:
              - A[0] < A[1] < ... A[i-1] < A[i]
              - A[i] > A[i+1] > ... > A[A.length - 1]
  - Edge case - array can be empty or less than 3 elements in array, 
              - multiple entries of max element, which makes array invalid for Mountain Array
              - max element could be last or first element in array
  - assumptions - 
  
Pseudo code - 
  - first check length of array, if less than 3, return False
  - 
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
# space complexity - O(1) - 
'''

# Solution 2 -
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
 
''' Big-O efficiency -
# time complexity - O(n) -- because of count function and for loop
# space complexity - O(1) -- memory usage is even better
'''
