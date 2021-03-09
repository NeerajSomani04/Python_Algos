## 378 -- https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Solution 1:
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        nums = [i for j in matrix for i in j]
        
        #heapq.heapify(nums) # creating a heapify is a O(log n) opertaion
        
        k_elements = [-x for x in nums[:k]]
        
        
        heapq.heapify(k_elements) # creating a heapify is a O(log n) opertaion [1,2]
        # remember this is min heap, hence, smallest element will always be at the top
        
        for i in range(k, len(nums)): # this is O(n) operation
            if -nums[i] > k_elements[0]:
                heapq.heappop(k_elements) # this is O(log k) operation
                heapq.heappush(k_elements,-nums[i]) # this is O(log k) operation
                
        return -list(k_elements)[-k]
        
        
        
        
'''
Time complexity #
The time complexity of this algorithm is O(K*logK+(N-K)*logK)O(K∗logK+(N−K)∗logK), which is asymptotically equal to O(N*logK)O(N∗logK)

Space complexity #
The space complexity will be O(K)O(K) because we need to store ‘K’ smallest numbers in the heap.
'''
