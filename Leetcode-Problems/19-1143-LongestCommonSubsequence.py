# In this we are going to solve leetcode #1143 problem
# https://leetcode.com/problems/longest-common-subsequence/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
# level order traversal meaning --> traversing left to right level by level
# This concept is also known as Breadth first search (BFS)

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a root node representing binary tree
  # Output -- return a number that represent depth/height of tree
  # Egde Cases -- "None" as root node or even at any level on any node
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 


''' Psudo code
  - create 2D tracker size m * n
    -- for every char in text1
      -- for every char in text2 
        -- if chars equal?, cell in diagonal + 1
        -- not? cell is max of above, left
    -- return last cell in tracker
'''

## Different approach
## Solution 1: using recursion and Depth First Search
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def maxDepth(self, root):
    if root is None:
      return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
time complexity --> O(n) --> we look every node once
    --> to be more specific for explaining, O(n + 2k), where n is total number of nodes in tree and k is number of leaf nodes for which we check left and right null value nodes as well, hence "2k". But at the its comes down to O(n).
    
space complexity --> O(k) --> where k is height of tree, because at any given time stack will hold only nodes at any given height.
'''
