# Solution 1: hash table
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
        majority = max(ht.values())
        for key, value in ht.items():
            if value == majority:
                return key

''' 
big-o efficiency
time complexity - O(n)
space complexity - O(n)
runtime - 176 ms
memory - 15.6 MB
'''

# Solution 2: "Boyer-Moore Voting Algorithm"
class Solution: 
    def majorityElement(self, nums: List[int]) -> int:
        c = v = 0
        for a in nums:
            if v == 0:
                c = a
            if c == a:
                v += 1
            else:
                v -= 1

        return c

  ''' 
big-o efficiency
time complexity - O(n)
space complexity - O(1)
runtime - 160 ms
memory - 15.6 MB
'''  
