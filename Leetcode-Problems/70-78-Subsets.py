## 78 -- https://leetcode.com/problems/subsets/


# Solution 1:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for currNum in nums:
            n = len(subsets)
            for i in range(n): 
                set1 = list(subsets[i])
                set1.append(currNum)
                subsets.append(set1)
        return subsets      


'''
Time complexity #
Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of O(2^N) subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the above algorithm will be O(N*2^N)

Space complexity #
All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, and each subset can take up to O(N)O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N)
'''
