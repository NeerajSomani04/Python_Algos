# In this we are going to solve leetcode #48 problem
# https://leetcode.com/problems/rotate-image/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given an n x n 2D matrix representing an image
  # Output -- No output return, as we are rotating the image by 90 degrees (clockwise), (in-place)
  # Egde Cases -- no edge cases
  # Assumptions -- Constraints:
        matrix.length == n
        matrix[i].length == n
        1 <= n <= 20
        -1000 <= matrix[i][j] <= 1000

## Notes - Mostly in 2-Dimensional array problems, either we traversing or transforming the array.


''' Pseudo code  --
      - reverse outer arrays
      - for each row
        - for each column flip co-ordinates
'''
   
    
# Actual code --
## Solution 1:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start = 0
        end = len(matrix)-1
        for i in range(len(matrix)):
            if start == end:
                break
            else:
                matrix[start], matrix[end] = matrix[end], matrix[start]
                start += 1
                end -= 1
            
        # above can be done using "matrix.reverse()"
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
