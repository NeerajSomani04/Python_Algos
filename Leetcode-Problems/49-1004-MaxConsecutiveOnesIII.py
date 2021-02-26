# 1004 - https://leetcode.com/problems/max-consecutive-ones-iii/

# Solution 1:
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        windowStart = 0
        max_len = 0
        count_1s = 0
        ht = {1:0, 0:0}
        for windowEnd in range(len(A)):
            ht[A[windowEnd]] += 1
            count_1s = ht[1]
            if windowEnd - windowStart + 1 - count_1s > K:
                ht[A[windowStart]] -= 1
                windowStart += 1
            max_len = max(max_len, sum(ht.values()))
        return max_len

'''
time complexity - O(n)
space complexity - O(1) - ht is a dictionary of constant space
'''
