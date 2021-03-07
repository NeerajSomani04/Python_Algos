## 1046 -- 


## Solution 1: python list recursive logic

class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        
        elif len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return abs(nums[0] - nums[1])
        
        else:
            max1 = max(nums)
            nums.remove(max1)
            max2 = max(nums)
            nums.remove(max2)
        
            if max1 != max2:
                val = abs(max1-max2)
                nums.append(val)

        val = self.lastStoneWeight(nums)
        return val

'''
time complexity - O(n) -- because we are 2 elements everytime and inserting one element
space complexity - O(n) -- because of recursive stack
'''

## Solution 2 : Simple sort loop procedure

def lastStoneWeight(self, stones: List[int]) -> int:
	for i in range(len(stones)-1):                # loop till the lastone remain
		stones.sort()                             # smash the heaviest, the heaviest to end of the list
		stones[-2] = abs(stones[-2] - stones[-1]) # y-x / 0 doent matter which one is bigger
		stones.pop()                              # Destroy the stone 
	return stones[0]                            # return the only element in the list

'''
time complexity - O(n) -- because we are 2 elements everytime and inserting one element
space complexity - O(n) -- because of recursive stack
'''

## Solution 3: heapify and priority queue is the best approach but i need more time to understand and implement them

'''
time complexity - O(log n) -- because priority queue with heap data structure only takes log n time
space complexity - O(n) -- because of recursive stack
'''

