## 744 - https://leetcode.com/problems/find-smallest-letter-greater-than-target/


# Solution 1:
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if letters[-1] <= target:
            return letters[0]
        
        low = 0
        high = len(letters) - 1
        
        while low <= high :
            mid = (low + high) // 2
            
            if letters[mid] <= target:
                low = mid+1  
            else:
                high = mid-1
        return letters[low]

'''
time complexity - O(log n)
space complexity - O(1)
'''

#solution 2:
def search_next_letter(letters, key):
  n = len(letters)
  if key < letters[0] or key > letters[n - 1]:
    return letters[0]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < letters[mid]:
      end = mid - 1
    else: # key >= letters[mid]:
      start = mid + 1

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  return letters[start % n]
'''
Time complexity 
Since, we are reducing the search range by half at every step, 
this means that the time complexity of our algorithm will be O(logN)O 
where ‘N’ is the total elements in the given array.
Space complexity 
The algorithm runs in constant space O(1).
'''
