# In this we are going to solve leetcode #102 problem
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
# level order traversal meaning --> traversing left to right level by level
# This concept is also known as Breadth first search (BFS)

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- a node, representing root of a Binary tree
  # Output -- return an array of array of numbers, where each sub-array representing one level (meaning sub-array contains nodes on each level in seperate array)
  # Egde Cases -- "None" as root node or Null as input
  # Assumptions -- if root is "None", return an empty array []
  

# important point about this solution:-
# BFS problems mostly requires a use of Queue concept. Because queue can hold the nodes of tree in specific order that we need to process. example, queue holds node from left to right and process them in FIFO order basis.
# hence, we run our algorithm untill our queue is empty. 

''' Psudo code:-
while the queue is not empty
--> set the bookmark, which is size of queue at every level
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
        level.append(item.val)
        if item.left != None: 
          queue.append(item.left)
        if item.right != None: 
          queue.append(item.right)
        size -= 0
      levels.append(level)
     return levels

'''
space complexity --> O(1) --> considering output levels array will always be there in any kind of solution, and level and queue will never go to n level and will always be comparativly small.
  -- also, it could be O(n) --> if we consider output array space in this calculation, the O(n+k), where n is number of nodes and k is maxinum size of queue.
time complexity --> O(n) --> because of upper while loop, inner while loop in only 'k' times which is maximum number of node at any given level.
'''

# Solution 2: Same solution, but different way of writing
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        Input - a root node of tree
        Output - a list of all nodes at each level
        Edge case - empty input, 
        assumption - 
        '''
        
        if root is None:
            return
        
        queue = [root]
        result = []
        
        while queue:
            len_q = len(queue)
            list_level = []
            while len_q > 0:
                curr = queue.pop(0)
                len_q -= 1
                list_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(list_level)
        
        return result
        
        
## Solution from grokking 



