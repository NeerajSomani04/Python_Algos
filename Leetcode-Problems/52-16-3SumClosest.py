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
space complexity - O(k) -- k will be mostly smaller than n, because of "result" 
'''
                    
        
