'''
Definition - from question itself
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

Data
  - input - two sorted integer array
  - ouput - one fully sorted array
  - edge cases - 
  - assumption - these assumptions provided in question itself
      -- The number of elements initialized in nums1 and nums2 are m and n respectively.
      -- You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Pseudo code -
  - num1 -- already has enough space to accomodate numbers from both array, hence we need to use O(1) space complexity
  - 

'''

# actual  code -
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while (m>0 and n>0):
            if nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1    
        nums1[:n] = nums2[:n]


## Big-O efficiency -
# time complexity - O(n) - because of while loop
# space complexity - O(1) 
          
