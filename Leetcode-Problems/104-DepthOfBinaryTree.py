# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
# level order traversal meaning --> traversing left to right level by level
# This concept is also known as Breadth first search (BFS)

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array contains binary tree nodes
  # Output -- return a number that represent depth/height of tree
  # Egde Cases -- "None" as root node or even at any level on any node
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 


''' Psudo code
if node is null, return 0
depth = max(go left, go right)
return 1+depth
'''

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

space complexity --> O(k) --> where k is height of tree, because at any given time stack will hold only nodes at any given height.
'''
  
  
  
