# In this we are going to solve leetcode #322 problem
# https://leetcode.com/problems/coin-change/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
'''
## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array reprensting coins denominations that allowed, and the amount
  # Output -- return a number that reqpresents total number of coins used for calculation
  # Egde Cases -- if amount is zero, return 0 and If that amount of money cannot be made up by any combination of the coins, return -1.
  # Assumptions -- array can't be empty
      Constraints:
        1 <= coins.length <= 12
        1 <= coins[i] <= 231 - 1
        0 <= amount <= 104
'''

Dynamic programming is all about --> a way to track, how a problem evolves over time, 

''' Psudo code
  - create dp array, size amount + 1
    - for each cell, index is amount
      - for each coin
        - "test" coin ("index" - coin + 1)
        - store best combination at index
        
        
  
'''

## Different approach
## Solution 1: 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + ([float('inf')] * amount)
        for i, val in enumerate(dp):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        min_coin = dp[-1]
        if min_coin == float('inf'):
            return -1
        return min_coin
        
'''
time complexity --> O(n * k) --> where n is amount and k in number coins, as we have nested for loop for these 2 items.
    
space complexity --> O(n) --> where n is amount
'''        
