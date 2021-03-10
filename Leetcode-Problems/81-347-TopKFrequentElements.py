## 347 - https://leetcode.com/problems/top-k-frequent-elements/

# Solution 1:
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHeap = []
        ht = {}
        for i in nums:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1
        
        for j in ht:
            heapq.heappush(myHeap, (-ht[j], j))
        
        #print(list(myHeap))
        result = []
        for t in range(k):
            result.append(heapq.heappop(myHeap)[1])
        return result

'''
Time complexity #
The time complexity of the above algorithm is O(N+N*logK)O(N+N∗logK).

Space complexity #
The space complexity will be O(N)O(N). Even though we are storing only ‘K’ numbers in the heap. For the frequency map, however, we need to store all the ‘N’ numbers.
'''
        
# Solution 2 :
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
    
        
'''
Time complexity #
The time complexity of the above algorithm is O(N+N*logK)O(N+N∗logK).

Space complexity #
The space complexity will be O(N)O(N). Even though we are storing only ‘K’ numbers in the heap. For the frequency map, however, we need to store all the ‘N’ numbers.
'''
