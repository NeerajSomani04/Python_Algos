# In this we are going to solve leetcode #121 problem
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement


## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array represent stock prices across different days
  # Output -- return a number that represent depth/height of tree
  # Egde Cases -- if stock prices continously go down and array items in decending order
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 


''' Psudo code
  - iterate left to right
    - update lowest (best buy price) in each step
    - calculate profite for the day
    - update best profit
  - return best profit
'''

## Different approach
## Solution 1: 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            profit = price - min_price
            if profit > best:
                best = profit
            if price < min_price:
                min_price = price
        return best

'''
time complexity --> O(n) --> only one for loop for array traversal
space complexity --> O(1) --> only 3 variables to store values
'''
