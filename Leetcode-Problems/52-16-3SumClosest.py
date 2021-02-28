# 16 - https://leetcode.com/problems/3sum-closest/

 '''
        ## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
          # Input -- an array nums of n integers, target sum value
          # Output -- return closest sum value
          # Egde Cases -- the solution set can contain duplicate intergers. 
          # Assumptions -- each input would have exactly one solution
            Constraints:
                3 <= nums.length <= 10^3
                -10^3 <= nums[i] <= 10^3
                -10^4 <= target <= 10^4
        '''

 
# Solution 1: below is my solution without any help, but looks like its not great solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        result = {target}
        for i in range(n):
            left = i+1
            right = n-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                elif total > target:
                    result.add(total)
                    right -= 1
                else:
                    result.add(total)
                    left += 1

        result = list(result)
        result.sort()
        #print(result)
        temp_i = 0
        for i, v in enumerate(result):
            if v == target:
                temp_i = i
                break
        #print(target, temp_i)
        if len(result) == 2 and temp_i == 0:
            return result[1]
        elif len(result) == 2 and temp_i == 1:
            return result[0]
        elif temp_i == 0:
            return result[1]
        elif temp_i == len(result)-1:
            return result[-2]
        elif abs(target-result[temp_i-1]) < abs(target-result[temp_i+1]):
            return result[temp_i-1]
        else:
            return result[temp_i+1]
        
'''
Big-O efficiency 
time complexity - O(n log n) -- considering sort function and for loop idea
space complexity - O(n) -- as sorting algorithm uses n space and for "result" set variable
'''
                    
## Solution : copied from leetcode
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if (diff == 0 || nums[i] + nums[i + 1] + nums[i + 2] > target):
                  break;
        return target - diff

'''
Complexity Analysis

Time Complexity: \mathcal{O}(n^2)O(n 
2
 ). We have outer and inner loops, each going through nn elements.

Sorting the array takes \mathcal{O}(n\log{n})O(nlogn), so overall complexity is \mathcal{O}(n\log{n} + n^2)O(nlogn+n 
2
 ). This is asymptotically equivalent to \mathcal{O}(n^2)O(n 
2
 ).

Space Complexity: from \mathcal{O}(\log{n})O(logn) to \mathcal{O}(n)O(n), depending on the implementation of the sorting algorithm.
'''
