class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for _ in nums:
            if len(str(_))%2 == 0:
                count += 1
        return count
        
        
'''
Big-O efficiency:-
# time complexity - O(n^2) because of O(n) for "for loop" and another O(n) for len function with-in for loop 
# space complexity - O(1)
