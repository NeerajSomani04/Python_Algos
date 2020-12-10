# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
# level order traversal meaning --> traversing left to right level by level
# This concept is also known as Breadth first search (BFS)

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array contains binary tree nodes
  # Output -- return an array of array that contain nodes on each level in seperate array
  # Egde Cases -- "None" as root node or even at any level on any node
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 

''' Psudo code:-
while the queue is not empty
--> set the bookmark
--> while bookmark > 0
    --> pull node from queue
    --> save value into level array
    --> add children to queue
'''


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def levelOrder(self, root):
    levels = []
    queue = [root]
    while queue:
      level = []
      size = len(queue)
      while size != 0 :
        item = queue.pop(0)
        level.append(item)
        if item.left != None: 
          queue.append(item.left)
        if item.right != None: 
          queue.append(item.right)
        size -= 0
      levels.append(level)
     return levels

'''
space complexity --> O(1) --> considering output levels array will always be there in any kind of solution, and level and queue will never go to n level and will always be comparativly small.

time complexity --> O(n) --> because of upper while loop, inner while loop in only 'k' times which is maximum number of node at any given level.

'''




