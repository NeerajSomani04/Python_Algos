## 704 -- 

'''
Constraints:
    1 <= nums.length <= 104
    -9999 <= nums[i], target <= 9999
    All the integers in nums are unique.
    nums is sorted in an ascending order.
'''

# Solution 1:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid-1
        
        return -1
                
'''
time complexity - O(log n) --> because we are travering and reducing our size everytime
space complexity - O(1) 
'''
            
            
        
