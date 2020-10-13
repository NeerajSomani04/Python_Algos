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

# solution 1:-
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights)<2:
            return 0
        temp = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if temp[i] != heights[i]:
                count += 1
        return count
        
''' Big-O efficiency:
# time complexity - O(n) - because of for loop
# space complexity - O(n) - because of another array
'''
