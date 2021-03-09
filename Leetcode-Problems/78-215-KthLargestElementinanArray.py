## 215 -- https://leetcode.com/problems/kth-largest-element-in-an-array/

# Solution 1:
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Edge cases -- numbers could be negative,
            -- numbers could be repetitive
            -- need to return kth largest item from array
        '''
        
        heapq.heapify(nums) # creating a heapify is a O(log n) opertaion
        
        k_elements = nums[:k]
        
        heapq.heapify(k_elements) # creating a heapify is a O(log n) opertaion [1,2]
        # remember this is min heap, hence, smallest element will always be at the top
        
        for i in range(k, len(nums)): # this is O(n) operation
            if nums[i] > k_elements[0]:
                heapq.heappop(k_elements) # this is O(log k) operation
                heapq.heappush(k_elements,nums[i]) # this is O(log k) operation
                
        return list(k_elements)[-k]
      
'''
time complexity - O(n log k) -- 
  -- which is better than sorting approach
space complexity - O(k)
'''
'''
Time complexity #
As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK)O(K∗logK+(N−K)∗logK), which is asymptotically equal to O(N*logK)O(N∗logK)

Space complexity #
The space complexity will be O(K)O(K) since we need to store the top ‘K’ numbers in the heap.
'''


'''
below code is to find kth smallest element in the array
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Edge cases -- numbers could be negative,
            -- numbers could be repetitive
            -- need to return kth largest item from array
        '''
        
        heapq.heapify(nums) # creating a heapify is a O(log n) opertaion
        
        k_elements = [-x for x in nums[:k]]
        
        heapq.heapify(k_elements) # creating a heapify is a O(log n) opertaion [1,2]
        # remember this is min heap, hence, smallest element will always be at the top
        
        for i in range(k, len(nums)): # this is O(n) operation
            if -nums[i] > k_elements[0]:
                heapq.heappop(k_elements) # this is O(log k) operation
                heapq.heappush(k_elements,nums[i]) # this is O(log k) operation
                
        return -list(k_elements)[-k]
        
        
        
        
       '''
