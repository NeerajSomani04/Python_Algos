## 90 -- 

# Solution 1:

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res
      
'''
Time complexity #
Since, in each step, the number of subsets doubles (if not duplicate) as we add each element to all the existing subsets, therefore, we will have a total of O(2^N)O(2
​N
​​ ) subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N)O(N∗2
​N
​​ ).

Space complexity #
All the additional space used by our algorithm is for the output list. Since, at most, we will have a total of O(2^N)O(2
​N
​​ ) subsets, and each subset can take up to O(N)O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N)O(N∗2
​N
​​ ).
'''
