  
# In this we are going to solve leetcode #119 problem
# https://leetcode.com/problems/pascals-triangle-ii/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an integer represents the row of pascal triangle
  # Output -- return element of input rowIndex
  # Egde Cases -- first row of pascal array
  # Assumptions -- rowIndex should be 0 or greater than 0


# Actual code --
# Solution 1:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            pascalArr = [1,1]
            counter = 1
            while rowIndex != counter:
                temp = []
                for i in range(len(pascalArr)-1):
                    temp.append(pascalArr[i] + pascalArr[i+1])
                temp = [1] + temp + [1]
                pascalArr = temp
                counter += 1
            return pascalArr

''' Big-O-efficiency
## time complexity - O(n) -- because we need to go to each row
## space complexity -- O(k) -- pascal array or temp array only holds elements k (row elements at any specific time)
'''
