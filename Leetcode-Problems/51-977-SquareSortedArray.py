# 977 -- https://leetcode.com/problems/squares-of-a-sorted-array/

'''
        Input - a sorted array of integers
        Output - a sorted array with squares of its original integers
        Edge - repetitive elements allowed
            - empty array not allowed as per constraints
        Assumptions -
        Constraints -
            1 <= nums.length <= 10^4
            -10^4 <= nums[i] <= 10^4
            nums is sorted in non-decreasing order.
        '''

# Solution 1:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        result = [0] * n
        result_heighest_index = n-1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq > right_sq:
                result[result_heighest_index] = left_sq
                left += 1
            else:
                result[result_heighest_index] = right_sq
                right -= 1
            result_heighest_index -= 1
        return result

# Solution 2:
answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer

  '''
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.
Space complexity 
The space complexity of the above algorithm will also be O(N); this space will be used for the output array.
'''
# Note - Need to search if this can be solved in O(1) space time.
