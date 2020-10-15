# Solution 1 -

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            intermediate = []
            for j in range(i+1):
                if j == 0 or j == i:
                    intermediate.append(1)
                else:
                    intermediate.append(result[i-1][j-1]+result[i-1][j])
            result.append(intermediate)
        return result

''' Big-O efficiency 
# time complexity - O(n*n) - because of 2 for loop
# space complexity - O(n) - because of intermediate array, space for result array is seperate
'''
