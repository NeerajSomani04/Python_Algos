# Below is my solution for practice problem: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

# This solution has :
# space complexity :: O(1)
# Time Complexity :: O(n)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: ## this is how we defined a function
        final = 0  ## created this variable to store the final count value of 1's that is maximum
        c = 0   ## created this variable to store the value of count of 1's as we go through the for loop
        for _ in nums:  ## loop is used to read each value of array one by one
            if _ == 0: ## checking the value of array as "0" to reset the counter
                c = 0
            else:
                c += 1 ## increment the counter value for all consecutive one's
            final = max(c,final) ## assigning max value to final variable in each iteration
        return final
