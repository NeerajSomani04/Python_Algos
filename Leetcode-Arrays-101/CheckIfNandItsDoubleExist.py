  
# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/)

Data - 
  - Input - a array that contains some intergers
  - output - return true if double exist, else False
  - Edge case - there could be one zero or zero available in array, need to consider this carefully.
  - assumptions - array would always have atleast 2 elements
       -  2 <= arr.length <= 500
       -  -10^3 <= arr[i] <= 10^3
  
Pseudo code - 
  - sort array (time complexity - n log n)
  - run through each element of array and apply BSA 
    - also make sure, i != j (this is critical edge case for 0, because 0*2 is also 0)
'''

# Actual Code 
# Solution 1 -
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort() # n log n
        for i in range(len(arr)):
            lo = 0
            hi = len(arr) - 1
            target_val = arr[i]*2
            while lo <= hi:
                mid = (lo+hi) // 2
                mid_val = arr[mid]
                print('arr_val=',arr[i], 'target=',target_val, 'lo=', lo, 'hi=', hi, 'mid=',mid)
                if target_val == mid_val and i != mid:
                    return True
                elif mid_val < target_val:
                    lo = mid+1
                else:
                    hi = mid-1
        return False
