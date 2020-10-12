# Lets follow our procedure to solve this question:

'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/)

Data - 
  - Input - a fixed length array that contains some intergers and a value that needs to be deleted from array
  - output - return final length of array after deleting value
  - Edge case - val element not at all present in array, all elements of the array are same as value, val element could be in start and end of the array
  - assumptions - array should not be empty
  
Pseudo code - 
    - read array and count number of occurance of val element.
    - reduce that count from array length, that will become our output array length
    - start reading elements of array from last,
        - if array element equals val, then increase val_count
        - else, place that specific array element towards end of array
  - read the array in reverse order and copy all elements as per output length array.
'''

# Actual Code 
# Solution 1:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        new_index = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                val_count += 1
            else:
                nums[new_index] = nums[i]
                new_index -= 1
        nums[:len(nums)-val_count:] = nums[val_count::]
        return len(nums)-val_count

''' Big-O efficiency:
time complexity - O(n) - because of for loop
space complexity - O(1) - constant space
'''
